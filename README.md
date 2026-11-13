# FastAPI Todo CRUD Application

A simple REST API application built using **Python, FastAPI, SQLAlchemy and SQLite** to manage Todo tasks through CRUD (Create, Read, Update and Delete) operations.

## Project Overview

The objective of this project is to understand backend application development using Python and FastAPI, implement REST APIs, interact with a relational database and build a structured, maintainable application.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Building REST APIs |
| SQLAlchemy | Database ORM and operations |
| SQLite | Relational database |
| Pydantic | Request and response validation |
| uv | Python project and dependency management |
| Swagger UI | API documentation and testing |

## Features

- Create new Todo tasks.
- Retrieve existing Todo records.
- Update existing Todo tasks.
- Manage task descriptions and completion status.
- Store Todo records in a SQLite database.
- Validate API requests and responses using Pydantic schemas.
- Perform database operations using SQLAlchemy ORM.
- Test API endpoints through Swagger UI.

## Project Structure

```text
todo_crud_app/
│
├── src/
│   └── todo_crud_app/
│       ├── __init__.py
│       ├── database.py
│       ├── models.py
│       ├── schemas.py
│       ├── crud.py
│       └── main.py
│
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

### Application Components

- **database.py:** Configures the SQLite database connection, SQLAlchemy engine, session and declarative base.
- **models.py:** Defines the Todo database model and its columns.
- **schemas.py:** Defines Pydantic schemas for request validation and API responses.
- **crud.py:** Contains the database operations for creating, retrieving and updating Todo records.
- **main.py:** Defines the FastAPI application and API endpoints.

## Prerequisites

- Python 3.11 or compatible version.
- uv package manager.
- Basic understanding of Python and REST APIs.

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-todo-crud-app.git
```

**2. Navigate to the project directory**

```bash
cd fastapi-todo-crud-app
```

**3. Install project dependencies**

```bash
uv sync
```

**4. Run the application**

```bash
uv run uvicorn todo_crud_app.main:app --reload
```

**5. Access the application**

API Base URL:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Database

The application uses SQLite as its database.

Todo records are stored in the `to_do_list` table.

The database is created locally when the application initializes its database configuration.

## Learning Objectives

Through this project, I am developing practical knowledge of:

- Python project structure and dependency management.
- REST API development using FastAPI.
- SQLAlchemy ORM and database sessions.
- Pydantic models and data validation.
- Implementing CRUD operations using a class-based approach.
- Connecting backend APIs with a relational database.
- Testing APIs using Swagger UI.
- Git and GitHub version control.

## Future Enhancements

- Implement DELETE functionality if not already completed.
- Add automated API testing using Pytest.
- Implement database migrations using Alembic.
- Add authentication and authorization.
- Explore asynchronous database operations.

---

**Author:** YOUR NAME

**Project:** FastAPI Todo CRUD Application