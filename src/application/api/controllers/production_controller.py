import inject
from fastapi import APIRouter
from fastapi.params import Depends

from src.domain.usecases.product.dtos.find_by_id_product_dto import FindByIdProductDto
from src.domain.usecases.product.product_find_by_id_uc import ProductFindByIdUC

route = APIRouter()

@route.post('/api/production/add_order', tags=["production"])
async def add_order():
    return {"message": "Order added successfully"}

@route.get('/api/production/get_product/{id}', tags=["production"])
@inject.autoparams()
async def get_product(id: int, product_find_by_id_uc: ProductFindByIdUC):
    product = await product_find_by_id_uc.execute(FindByIdProductDto(id=id))

    if not product:
        return {"message": "Produto não encontrado"}

    return product