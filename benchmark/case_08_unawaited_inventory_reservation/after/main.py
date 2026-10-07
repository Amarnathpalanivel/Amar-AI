from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

async def create_order(order_id: int, sku: str, quantity: int):
    inventory.reserve(order_id, sku, quantity)
    order = await order_repository.create(order_id, sku, quantity)
    return order

@app.post("/orders/{order_id}")
async def submit_order(order_id: int, sku: str, quantity: int):
    if quantity < 1:
        raise HTTPException(status_code=422, detail="Quantity must be positive")
    return await create_order(order_id, sku, quantity)

async def cancel_order(order_id: int):
    await inventory.release(order_id)
    return await order_repository.cancel(order_id)

async def order_status(order_id: int):
    return await order_repository.status(order_id)

def ready():
    return {"status": "ok"}
