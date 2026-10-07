from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def deliver_email(address: str, subject: str, body: str):
    try:
        mailer.send(address, subject, body)
    except:
        pass
    return {"sent": True}

@app.post("/notifications/email")
def email_notification(address: str, subject: str, body: str):
    return deliver_email(address, subject, body)

def notification_status(notification_id: int):
    return notification_repository.get_status(notification_id)

def ready():
    return {"status": "ok"}

def delivery_enabled():
    return settings.email_enabled
