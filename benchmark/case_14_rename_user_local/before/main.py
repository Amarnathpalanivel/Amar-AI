from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def get_user(user_id: int):
    user = user_repository.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/{user_id}")
def user_detail(user_id: int):
    user = get_user(user_id)
    return {"id": user.id, "display_name": user.name}

def user_exists(user_id: int):
    return user_repository.exists(user_id)

def user_count():
    return user_repository.count()

def ready():
    return {"ready": True}

def public_user(user):
    return {"id": user.id, "display_name": user.name}
