from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def subtotal(items):
    total = 0
    for item in items:
        total += item.price * item.quantity
    return round(total, 2)

def cart_subtotal(items):
    return subtotal(items)

@app.post("/cart/total")
def cart_total(cart: Cart):
    return {"subtotal": cart_subtotal(cart.items)}

def tax_for(subtotal: float, rate: float):
    return round(subtotal * rate, 2)

def ready():
    return {"ready": True}

def item_count(cart):
    return sum(item.quantity for item in cart.items)
