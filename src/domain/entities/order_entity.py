from datetime import datetime

from src.domain.entities.base_entity import BaseEntity
from src.domain.entities.combo_entity import ComboEntity
from src.domain.entities.customer_entity import CustomerEntity
from src.domain.enums.order_status_enum import OrderStatusEnum


class OrderEntity(BaseEntity):
    combos: list[ComboEntity]
    total_price: float
    status: OrderStatusEnum = OrderStatusEnum.RECEIVED
    finished_time: datetime

    # Relations
    id_customer: int

    # Nested Objects
    customer: CustomerEntity | None = None