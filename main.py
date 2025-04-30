from fastapi import FastAPI
from routers import todo_api

app = FastAPI()

app.include_router(todo_api.router)