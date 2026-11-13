from sqlalchemy import Column, String, Text, DateTime, Integer
from .database import Base
from datetime import datetime

class Todo(Base):
    __tablename__ = 'to_do_list'

    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
# datetime.now() executes immediately when the class is defined.
# datetime.now passes the function itself to SQLAlchemy, allowing it to execute whenever a new
# record is inserted.
# This is an important Python concept: passing a function versus calling a function.

#variable