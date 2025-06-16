from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.connection import SessionLocal
from query import crud
from schemas import item

from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/todos", response_model=List[item.ToDoItem])
def get_todos(db: Session = Depends(get_db)):
    return crud.all_todos(db)

@router.post("/todos", response_model=item.ToDoItem)
def add_todo(todo: item.ToDoInputItem, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

@router.patch("/todos/{id}", response_model=item.ToDoItem)
def completed_todo(id: int, completed: item.ToDoCompletedUpdate, db: Session = Depends(get_db)):
    return crud.update_completed_todo(id=id, completed=completed.completed, db=db)

@router.delete("/todos/{id}", response_model=item.ToDoItem)
def deleted_todo(id:int, db: Session = Depends(get_db)):
    return crud.delete_todo(id=id, db=db)