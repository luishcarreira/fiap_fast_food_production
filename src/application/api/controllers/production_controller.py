from fastapi import APIRouter, HTTPException

from src.domain.usecases.order.dtos.create_order_dto import CreteOrderDto
from src.domain.usecases.order.send_order_to_queue_uc import SendOrderToQueueUC
from src.domain.usecases.product.dtos.find_by_id_product_dto import FindByIdProductDto
from src.domain.usecases.product.product_find_by_id_uc import ProductFindByIdUC

route = APIRouter()

@route.post('/api/production/add_order', tags=["production"])
async def add_order(order: CreteOrderDto):
    try:
        await SendOrderToQueueUC().execute("fiap_fast_food_order_for_production", order)
        return {"message": "Order added successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error adding order to queue: {str(e)}"
        )

@route.get('/api/production/get_product/{id}', tags=["production"])
async def get_product(id: int):
    product = await ProductFindByIdUC.execute(FindByIdProductDto(id=id))

    if not product:
        return {"message": "Produto não encontrado"}

    return product