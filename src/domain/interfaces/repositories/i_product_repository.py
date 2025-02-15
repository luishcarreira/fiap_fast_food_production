from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.product_entity import ProductEntity


class IProductRepository(ABC):

    @abstractmethod
    async def get(self, product_id: int) -> Optional[ProductEntity]:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, product_entity: ProductEntity) -> Optional[ProductEntity]:
        raise NotImplementedError()