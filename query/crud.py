from sqlalchemy.orm import Session
from models.todo import ToDo
from schemas import item
from datetime import datetime
from fastapi import HTTPException

def all_todos(db: Session):
    return db.query(ToDo).all()

def create_todo(db: Session, todo: item.ToDoInputItem):
    db_todo = ToDo(
        **todo.model_dump(),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.add(db_todo)
    db.commit()

    return db_todo

def update_completed_todo(db: Session, id: int, completed: str):
    todo_item = db.query(ToDo).filter(ToDo.id == id).first()

    if not todo_item:
        raise HTTPException(status_code=404, detail="The provided ID does not exist")
    
    todo_item.completed = completed
    db.commit()

    return todo_item

def delete_todo(db: Session, id: int):
    todo_item=db.query(ToDo).filter(ToDo.id==id).first()

    if not todo_item:
        raise HTTPException(status_code=404, detail="The provided ID does not exist")

    db.delete(todo_item)
    db.commit()

    return todo_item
