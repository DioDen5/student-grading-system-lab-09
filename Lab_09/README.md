# Лабораторна робота №9

**Тема:** Concurrency, parallelism, profiling та оптимізація  
**Студент:** Заставний Денис, ФеП-32  
**Предмет:** professional_python  
**Варіант:** 7 — система оцінювання студентів

## Реалізовано

- baseline analytics на Python loops;
- NumPy vectorization для статистики 1 000 000 оцінок;
- ThreadPoolExecutor для I/O-bound імпорту CSV;
- ProcessPoolExecutor для CPU-bound обчислень;
- synchronization спільного стану через `threading.Lock`;
- caching академічної статистики з hit/miss та invalidation;
- вимірювання `perf_counter`, cProfile і tracemalloc;
- benchmark для 10 000, 100 000 та 1 000 000 оцінок;
- порівняння workers 1, 2, 4 і обчислення speedup;
- correctness tests для всіх optimized implementations.

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[test]'
pytest -v
python tools/run_experiment.py
```

Результати експерименту зберігаються в `benchmarks/results/`.

Звіт: [`report/report.docx`](report/report.docx).
