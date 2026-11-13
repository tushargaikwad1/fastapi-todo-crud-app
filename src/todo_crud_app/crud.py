from .models import Todo
# from .database import SessionLocal

# db = SessionLocal()

class TodoCRUD:
    def __init__(self, db):
        self.db = db
    
    def create_todo(self, todo_data):
        todo = Todo(
            task=todo_data.task,
            description=todo_data.description,
            status=todo_data.status
        )
        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)

        return todo

    def get_todos(self):
        return self.db.query(Todo).all()

    def get_todo_by_id(self, todo_id):
        return self.db.query(Todo).filter(Todo.id == todo_id).first()

    def update_todo(self, todo_id, update_data):
        todo = self.get_todo_by_id(todo_id)

        if todo is None:
            return None

        update_dict = update_data.model_dump(exclude_unset=True)
        # model_dump return a dictionary and hence we need to capture it.

        for key, value in update_dict.items():
            setattr(todo, key, value)
            # SYNTAX: settattr(object, attribute_name, new_value)
        
        self.db.commit()
        self.db.refresh(todo)

        return todo

    def delete_todo(self, todo_id):
        todo = self.get_todo_by_id(todo_id)

        if todo is None:
            return None

        self.db.delete(todo)
        self.db.commit()

        return True
    