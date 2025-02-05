from sqlalchemy.orm import Session

from src.domain.entities.order_entity import OrderEntity
from src.domain.interfaces.i_order_repository import IOrderRepository
from src.infra.models.order_model import OrderModel
from src.infra.utils.generic_mapper import GenericMapper


class OrderRepository(IOrderRepository):
    def __init__(self, session: Session):
        self._session = session

    def get(self, order_id: int) -> OrderEntity | None:
        order_model = self._session.query(OrderModel).filter(OrderModel.id == order_id).first()
        return GenericMapper.to_entity(order_model, OrderEntity) if order_model else None

    def create(self, order: OrderEntity) -> int | None:
        pass

    def update(self, order: OrderEntity) -> bool | None:
        pass