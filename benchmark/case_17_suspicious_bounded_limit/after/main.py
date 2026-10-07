from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def list_events(limit: int, cursor: Optional[str]):
    return event_repository.list(limit=limit, cursor=cursor)

@app.get("/events")
def events(limit: int = 50, cursor: Optional[str] = None):
    page_size = min(max(limit, 1), 200)
    normalized_cursor = normalize_cursor(cursor)
    return list_events(page_size, normalized_cursor)

def event_count():
    return event_repository.count()

def event_detail(event_id: str):
    return event_repository.get(event_id)

def ready():
    return {"ready": True}

def normalize_cursor(cursor: Optional[str]):
    return cursor.strip() if cursor else None

def format_event(event):
    return {"id": event.id, "created_at": event.created_at}
