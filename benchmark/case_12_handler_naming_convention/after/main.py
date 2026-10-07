from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    customer = customer_repository.get(customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.get("/customers/{customer_id}/orders")
def get_customer_orders(customer_id: int):
    return order_repository.for_customer(customer_id)

@app.get("/customers/{customer_id}/status")
def getCustomer(customer_id: int):
    return customer_repository.status(customer_id)

def serialize_customer(customer):
    return {"id": customer.id, "name": customer.name}

def customer_is_active(customer_id: int):
    return customer_repository.is_active(customer_id)

def customer_count():
    return customer_repository.count()
