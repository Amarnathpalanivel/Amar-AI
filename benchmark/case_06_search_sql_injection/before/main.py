from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def search_customers(term: str):
    query = text("SELECT id, name FROM customers WHERE name LIKE :term")
    return database.execute(query, {"term": f"%{term}%"}).fetchall()

@app.get("/customers/search")
def customer_search(term: str):
    if len(term) > 100:
        raise HTTPException(status_code=422, detail="Search term too long")
    rows = search_customers(term)
    return [{"id": row.id, "name": row.name} for row in rows]

def customer_count():
    return database.scalar(text("SELECT count(*) FROM customers"))

def ready():
    return {"ready": database.is_connected()}

def normalize_term(term: str):
    return term.strip()
