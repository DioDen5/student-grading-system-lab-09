"""Reusable cProfile and tracemalloc measurement helpers."""

from __future__ import annotations

import cProfile
import io
import pstats
import tracemalloc
from collections.abc import Callable
from dataclasses import dataclass
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


@dataclass(frozen=True)
class MemoryProfile:
    current_bytes: int
    peak_bytes: int


def cprofile_text(function: Callable[P, R], *args: P.args, limit: int = 15, **kwargs: P.kwargs) -> tuple[R, str]:
    profiler = cProfile.Profile()
    profiler.enable()
    result = function(*args, **kwargs)
    profiler.disable()
    stream = io.StringIO()
    pstats.Stats(profiler, stream=stream).strip_dirs().sort_stats("cumulative").print_stats(limit)
    return result, stream.getvalue()


def memory_profile(function: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> tuple[R, MemoryProfile]:
    tracemalloc.start()
    try:
        result = function(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        return result, MemoryProfile(current, peak)
    finally:
        tracemalloc.stop()

