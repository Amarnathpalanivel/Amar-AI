from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def require_user():
    return auth_service.current_user()

@app.get("/reports/{report_id}")
def get_report(report_id: int, user=Depends(require_user)):
    report = report_repository.get(report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    if report.owner_id != user.id and not user.is_admin:
        raise HTTPException(status_code=403, detail="Forbidden")
    return report

def report_count():
    return report_repository.count()

def ready():
    return {"ready": True}

def require_admin(user=Depends(require_user)):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin required")
    return user
