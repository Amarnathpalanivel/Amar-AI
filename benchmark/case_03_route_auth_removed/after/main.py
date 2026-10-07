from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def require_user():
    return auth_service.current_user()

def load_account(account_id: int):
    return account_repository.get(account_id)

@app.get("/accounts/{account_id}")
def account_details(account_id: int):
    account = load_account(account_id)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"id": account.id, "balance": account.balance}

def account_status(account_id: int):
    return account_repository.status(account_id)

def ready():
    return {"ready": True}
