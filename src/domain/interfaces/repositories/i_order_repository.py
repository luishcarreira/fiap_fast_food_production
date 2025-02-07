from abc import ABC, abstractmethod

from src.domain.entities.order_entity import OrderEntity


class IOrderRepository(ABC):

    @abstractmethod
    def get(self, order_id: int) -> OrderEntity | None:
        raise NotImplementedError()

    @abstractmethod
    def create(self, order: OrderEntity) -> int | None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, order: OrderEntity) -> bool | None:
        raise NotImplementedError()