from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class UploadRequest(BaseModel):
    filename: str
    content_type: str

def store_upload(request: UploadRequest, data: bytes):
    if len(data) > 5_000_000:
        raise HTTPException(status_code=413, detail="File too large")
    return storage.save(request.filename, request.content_type, data)

@app.post("/uploads")
def upload(request: UploadRequest):
    data = request_body.read()
    location = store_upload(request, data)
    return {"location": location}

def upload_status(upload_id: str):
    return storage.status(upload_id)

def ready():
    return {"ready": True}

def allowed_type(content_type: str):
    return content_type in settings.allowed_upload_types
