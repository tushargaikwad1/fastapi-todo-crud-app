from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TodoCreate(BaseModel):
    task:str
    description:str | None=None
    status:str

class TodoUpdate(BaseModel):
    description:str | None=None
    status:str | None=None

class TodoResponse(BaseModel):
    id:int
    task:str
    description:str
    status:str
    created_at:datetime

    model_config=ConfigDict(from_attributes=True)