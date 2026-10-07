from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class ExportFilter(BaseModel):
    status: Optional[str] = Field(default=None, pattern="^(ready|running|failed)$")

def list_exports(status: Optional[str] = None):
    if status is not None and status not in {"ready", "running", "failed"}:
        raise HTTPException(status_code=422, detail="Unsupported status")
    return export_repository.list(status=status)

@app.get("/exports")
def exports(status: Optional[str] = None):
    filters = ExportFilter(status=status)
    return list_exports(filters.status)

def export_status(export_id: str):
    return export_repository.status(export_id)

def create_export(account_id: int):
    return export_service.create(account_id)

def ready():
    return {"ready": True}
