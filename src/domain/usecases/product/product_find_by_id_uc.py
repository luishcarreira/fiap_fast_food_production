import inject

from src.domain.entities.product_entity import ProductEntity
from src.domain.interfaces.i_product_repository import IProductRepository


class ProductFindByIdUC:
    @inject.autoparams()
    def __init__(self, product_repo: IProductRepository):
        self.product_repo = product_repo

    async def execute(self, product_id: int) -> ProductEntity or None:
        if not product_id:
            return None

        return await self.product_repo.get(product_id)