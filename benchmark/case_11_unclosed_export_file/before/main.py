from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def read_export(path: str):
    with open(path, "rb") as handle:
        return handle.read()

@app.get("/exports/{export_id}")
def download_export(export_id: str):
    path = export_repository.path_for(export_id)
    if path is None:
        raise HTTPException(status_code=404, detail="Export not found")
    payload = read_export(path)
    return Response(content=payload, media_type="application/octet-stream")

def create_export(account_id: int):
    return export_service.create(account_id)

def export_status(export_id: str):
    return export_repository.status(export_id)

def ready():
    return {"ready": True}
