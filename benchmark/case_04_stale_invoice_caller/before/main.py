from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def create_invoice(customer_id: int, amount: float):
    return invoice_service.create(customer_id, amount, "USD")

def invoice_for_order(order):
    return create_invoice(order.customer_id, order.total)

def invoice_for_subscription(subscription):
    return create_invoice(subscription.customer_id, subscription.price)

def legacy_invoice(customer_id: int, amount: float):
    return create_invoice(customer_id, amount)

@app.post("/invoices/order/{order_id}")
def order_invoice(order_id: int):
    order = order_service.get(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return invoice_for_order(order)

def invoice_status(invoice_id: int):
    return invoice_service.status(invoice_id)

def health():
    return {"status": "ok"}
