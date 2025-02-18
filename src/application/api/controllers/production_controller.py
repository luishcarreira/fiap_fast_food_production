from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from src.domain.usecases.order.dtos.create_order_dto import CreateOrderDto
from src.domain.usecases.order.order_create_uc import OrderCreateUC
from src.domain.usecases.order.send_order_to_queue_uc import SendOrderToQueueUC

route = APIRouter()

@route.post('/api/production/add_order', tags=["production"])
async def add_order(order: CreateOrderDto):
    try:
        await OrderCreateUC().execute(order)
        return {"message": "Order added successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error adding order to queue: {str(e)}"
        )