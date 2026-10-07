from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

PAYMENTS_API_KEY = "sk_live_4f8b2c9d7a1e"

def payment_headers():
    return {"Authorization": f"Bearer {PAYMENTS_API_KEY}"}

def submit_payment(payload):
    response = http_client.post(
        settings.payment_url,
        json=payload,
        headers=payment_headers(),
        timeout=5,
    )
    response.raise_for_status()
    return response.json()

@app.post("/payments")
def create_payment(payload: dict):
    return submit_payment(payload)

def provider_ready():
    return bool(PAYMENTS_API_KEY)
