from .database import SessionLocal, Base, db_engine
from .models import Todo
from .schemas import TodoCreate, TodoUpdate, TodoResponse
from .crud import TodoCRUD
from fastapi import FastAPI, Depends, HTTPException

Base.metadata.create_all(bind=db_engine)        # This instructs SQLAlchemy to create all registered tables that don't already exist.

print("Registered tables:", Base.metadata.tables.keys())

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post('/new_to_do', response_model=TodoResponse, status_code=201)
def create_todo(todo_data: TodoCreate, db=Depends(get_db)):
    todo_crud = TodoCRUD(db)
    return todo_crud.create_todo(todo_data)

@app.get('/to_do_list', response_model=list[TodoResponse])
def get_todos(db=Depends(get_db)):
    todo_crud = TodoCRUD(db)
    return todo_crud.get_todos()

@app.get('/to_do', response_model=TodoResponse)
def get_todo(todo_id: int, db=Depends(get_db)):
    todo_crud = TodoCRUD(db)
    todo = todo_crud.get_todo_by_id(todo_id)

    if todo is None:
        raise HTTPException(status_code=404, detail="Details not found")
    else:
        return todo

@app.put('/to_do_list/{todo_id}', response_model=TodoResponse)
def update_todo(todo_id: int, todo_data: TodoUpdate, db=Depends(get_db)):
    todo_crud = TodoCRUD(db)
    todo = todo_crud.update_todo(todo_id, todo_data)

    if todo is None:
        raise HTTPException(status_code=404, detail="To-Do not found")

    return todo

@app.delete('/to_do_list/{todo_id}')
def delete_todo(todo_id: int, db=Depends(get_db)):
    todo_crud = TodoCRUD(db)
    result = todo_crud.delete_todo(todo_id)

    if result is None:
        raise HTTPException(status_code=404, detail="To-Do not found")
    else:
        return {"message": "To-Do deleted successfully"}