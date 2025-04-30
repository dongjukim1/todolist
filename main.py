from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI()

class ToDoInputItem(BaseModel):
    title: str
    description: str = None
    

class ToDoItem(ToDoInputItem):
    id: int
    last_modified_at: datetime
    completed: bool = False

todo_list =[]
init_id = 0

@app.get('/todos', response_model=List[ToDoItem])
def get_todo():
    return todo_list

@app.post('/todos', response_model=ToDoItem)
def add_todo(todo: ToDoInputItem):
    global init_id
    init_id+=1

    now = datetime.now()
    todo_item = ToDoItem(id=init_id, last_modified_at=now, **todo.model_dump())
    todo_list.append(todo_item)

    return todo_item

@app.patch('/todos/{id}', response_model=ToDoItem)
def update_todo(id: int):
    if id<=0 or id>len(todo_list): 
        raise HTTPException(status_code=404, detail="The provided ID does not exist")
    
    for idx, item in enumerate(todo_list):
        if(item.id == id):
            item.completed = True
            item.last_modified_at = datetime.now()
            return item

@app.delete('/todos/{id}', response_model=ToDoItem)
def delete_todo(id: int):
    if id<=0 or id>len(todo_list):
        raise HTTPException(status_code=404, detail="The provided ID does not exist")
    
    for idx, item in enumerate(todo_list):
        if(item.id == id):
            todo = todo_list.pop(idx)
            break

    return todo


