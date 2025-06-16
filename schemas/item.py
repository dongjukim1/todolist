from pydantic import BaseModel
from datetime import datetime
from typing import Literal


Stage = Literal["Pending", "In Progress", "Completed"]

class ToDoInputItem(BaseModel):
    title: str
    description: str = None
    

class ToDoItem(ToDoInputItem):
    id: int
    created_at: datetime
    updated_at: datetime
    completed: Stage ="Pending"

class ToDoCompletedUpdate(BaseModel):
    completed: Stage
