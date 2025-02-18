from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.order_entity import OrderEntity
from src.domain.enums.production_status_enum import ProductionStatusEnum


class IOrderRepository(ABC):

    @abstractmethod
    async def get(self, id_order: int) -> Optional[OrderEntity]:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, order: OrderEntity) -> Optional[OrderEntity]:
        raise NotImplementedError()

    @abstractmethod
    async def update_status(self, id_order: int, status: ProductionStatusEnum) -> Optional[bool]:
        raise NotImplementedError()