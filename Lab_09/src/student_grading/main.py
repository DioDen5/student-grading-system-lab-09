"""Run the FastAPI application with Uvicorn."""

import uvicorn


def main() -> None:
    uvicorn.run("student_grading.api:app", host="127.0.0.1", port=8000, reload=False)


if __name__ == "__main__":  # pragma: no cover - exercised through __main__.py
    main()
