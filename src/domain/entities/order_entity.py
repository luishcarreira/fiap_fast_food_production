from datetime import datetime

from src.domain.entities.base_entity import BaseEntity
from src.domain.entities.combo_entity import ComboEntity
from src.domain.enums.order_status_enum import OrderStatusEnum


class OrderEntity(BaseEntity):
    combos: list[ComboEntity]
    status: OrderStatusEnum = OrderStatusEnum.RECEIVED
    start_time: datetime
    finished_time: datetime