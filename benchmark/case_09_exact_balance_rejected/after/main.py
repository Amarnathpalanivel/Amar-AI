from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def withdraw(account, amount: float):
    if amount <= 0:
        raise HTTPException(status_code=422, detail="Amount must be positive")
    if account.balance <= amount:
        raise HTTPException(status_code=409, detail="Insufficient funds")
    account.balance -= amount
    ledger.record(account.id, -amount)
    return {"balance": account.balance}

@app.post("/accounts/{account_id}/withdraw")
def withdraw_from_account(account_id: int, amount: float):
    account = account_repository.get_for_update(account_id)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return withdraw(account, amount)

def balance(account_id: int):
    return account_repository.balance(account_id)

def ready():
    return {"ready": True}
