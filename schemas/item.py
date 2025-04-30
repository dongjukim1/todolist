from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ToDoInputItem(BaseModel):
    title: str
    description: str = None
    

class ToDoItem(ToDoInputItem):
    id: int
    created_at: datetime
    updated_at: datetime
    completed: bool = False