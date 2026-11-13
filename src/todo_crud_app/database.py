from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
# when we use .parent is points to todo_crud_app (Python Package) inside src folder but we need to
# create database inside todo_crud_app which is the Project Root folder.
# To reach project root folder we need to move 2 steps above.

DB_PATH = BASE_DIR / 'todo.db'

# print("BASE_DIR:", BASE_DIR)
# print("DB_PATH:", DB_PATH)

DATABASE_URL = f"sqlite:///{DB_PATH.as_posix()}"
# as_posix() - It converts Windows backslashes into forward slashes, making the path suitable for
# SQLAlchemy's SQLite URL.

db_engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
# create_engine(): Creates the SQLAlchemy engine, which manages communication with SQLite.
# check_same_thread=False: Allows SQLite connections to be used across different threads, which is 
# useful when working with FastAPI.

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=db_engine
)
# sessionmaker	    SQLAlchemy function that creates a session factory.
# SessionLocal	    Our session factory.
# autocommit=False	Changes are not automatically committed to the database.
# autoflush=False	SQLAlchemy does not automatically flush pending changes before queries.
# bind=engine	    Connects the sessions to our SQLite database engine.
# SessionLocal is not an actual database session. It's a factory that creates sessions when called,
#  like db=SessionLocal().

class Base(DeclarativeBase):
    pass