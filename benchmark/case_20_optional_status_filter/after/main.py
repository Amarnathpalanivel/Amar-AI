from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def find_tasks(status: Optional[str]):
    return task_repository.list(status=status)

@app.get("/tasks")
def tasks(status: Optional[str] = None):
    return find_tasks(status)

def task_count(status: Optional[str] = None):
    return task_repository.count(status=status)

def task_detail(task_id: int):
    return task_repository.get(task_id)

def ready():
    return {"ready": True}

def allowed_statuses():
    return {"open", "done", "blocked"}
