from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def receive_webhook(payload: dict):
    try:
        return webhook_service.process(payload)
    except WebhookSignatureError as exc:
        raise HTTPException(status_code=401, detail="Invalid signature") from exc

@app.post("/webhooks/provider")
def provider_webhook(payload: dict):
    return receive_webhook(payload)

def webhook_status(event_id: str):
    return webhook_repository.status(event_id)

def ready():
    return {"ready": True}

def provider_enabled():
    return settings.provider_enabled

def event_count():
    return webhook_repository.count()
