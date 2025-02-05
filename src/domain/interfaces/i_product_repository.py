from abc import ABC, abstractmethod

from src.domain.entities.product_entity import ProductEntity


class IProductRepository(ABC):

    @abstractmethod
    async def get(self, product_id: int) -> ProductEntity | None:
        raise NotImplementedError()

    # @abstractmethod
    # def create(self, product: ProductEntity) -> int | None:
    #     raise NotImplementedError()
    #
    # @abstractmethod
    # def update(self, product: ProductEntity) -> bool | None:
    #     raise NotImplementedError()