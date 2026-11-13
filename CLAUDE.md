# Project: FastAPI CRUD POC
Learning project: FastAPI + SQLAlchemy + SQLite (todo app). Goal is to understand
API development, DB connectivity and CRUD, with sound design and strong foundations.

# Run
- `uv run uvicorn todo_crud_app.main:app --reload` (run from this folder)
- Python >=3.13, managed with uv. Code is in `src/todo_crud_app/`.
- DB file is `todo.db` in this folder, table `to_do_list`.

# Files
- main.py (routes), crud.py (DB logic), models.py, schemas.py, database.py

# How to help here
- When changing code, explain what changes in which file and why, tied to my issue.
- Keep my existing comments and style.
- Notes I'm building should explain why each file, function and parameter exists, without repeating myself.
- Possible later steps: automated tests, migration to PostgreSQL (not decided).
