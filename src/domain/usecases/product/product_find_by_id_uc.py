import inject

from src.domain.entities.product_entity import ProductEntity
from src.domain.interfaces.repositories.i_product_repository import IProductRepository
from src.domain.usecases.product.dtos.find_by_id_product_dto import FindByIdProductDto


class ProductFindByIdUC:
    @inject.autoparams()
    def __init__(self, product_repo: IProductRepository):
        self.product_repo = product_repo

    async def execute(self, find_by_id_product_dto: FindByIdProductDto) -> ProductEntity or None:
        if not find_by_id_product_dto.id:
            return None

        return await self.product_repo.get(find_by_id_product_dto.id)