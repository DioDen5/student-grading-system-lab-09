import pytest

from student_grading.database import (
    create_schema,
    create_sqlite_engine,
    make_session_factory,
    session_scope,
)
from student_grading.main import main
from student_grading.models import Student


def test_session_scope_commits(tmp_path):
    engine = create_sqlite_engine(tmp_path / "commit.db")
    create_schema(engine)
    factory = make_session_factory(engine)
    with session_scope(factory) as session:
        session.add(Student(full_name="Committed"))
    with factory() as session:
        assert session.query(Student).one().full_name == "Committed"


def test_session_scope_rolls_back(tmp_path):
    engine = create_sqlite_engine(tmp_path / "rollback.db")
    create_schema(engine)
    factory = make_session_factory(engine)
    with pytest.raises(RuntimeError):
        with session_scope(factory) as session:
            session.add(Student(full_name="Rolled back"))
            session.flush()
            raise RuntimeError("failure")
    with factory() as session:
        assert session.query(Student).count() == 0


def test_main_starts_uvicorn(monkeypatch):
    calls = []
    monkeypatch.setattr("student_grading.main.uvicorn.run", lambda *args, **kwargs: calls.append((args, kwargs)))
    main()
    assert calls == [(("student_grading.api:app",), {"host": "127.0.0.1", "port": 8000, "reload": False})]
