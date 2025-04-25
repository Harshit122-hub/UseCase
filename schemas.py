from pydantic import BaseModel
from datetime import date

class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: date

class TaskUpdate(BaseModel):
    done: bool

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    due_date: date
    done: bool

    class Config:
        from_attributes = True
