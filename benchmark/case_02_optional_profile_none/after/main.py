from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def get_user(user_id: int):
    return repository.find_user(user_id)

@app.get("/users/{user_id}/email")
def user_email(user_id: int):
    user = get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"email": user.profile.email}

def user_summary(user):
    return {"id": user.id, "name": user.name}

def active_user_count():
    return repository.count_active()

def repository_health():
    return repository.is_ready()
