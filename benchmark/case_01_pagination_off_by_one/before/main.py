from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def list_records(rows, page: int, limit: int):
    page = max(page, 0)
    limit = min(max(limit, 1), 100)
    offset = page * limit
    if offset >= len(rows):
        return []
    return rows[offset : offset + limit]

@app.get("/records")
def records(page: int = 0, limit: int = 20):
    rows = load_records()
    return list_records(rows, page, limit)

def load_records():
    return [{"id": index} for index in range(250)]

def record_count():
    return len(load_records())

def health():
    return {"status": "ok"}
