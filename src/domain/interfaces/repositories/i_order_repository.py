from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.order_entity import OrderEntity


class IOrderRepository(ABC):

    @abstractmethod
    async def get(self, order_id: int) -> Optional[OrderEntity]:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, order: OrderEntity) -> Optional[OrderEntity]:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, order: OrderEntity) -> Optional[OrderEntity]:
        raise NotImplementedError()