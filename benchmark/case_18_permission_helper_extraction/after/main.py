from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def require_user():
    return auth_service.current_user()

def can_view_report(report, user):
    return report.owner_id == user.id or user.is_admin

@app.get("/reports/{report_id}")
def get_report(report_id: int, user=Depends(require_user)):
    report = report_repository.get(report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    if not can_view_report(report, user):
        raise HTTPException(status_code=403, detail="Forbidden")
    return report

def report_count():
    return report_repository.count()

def ready():
    return {"ready": True}
