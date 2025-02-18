from datetime import datetime
from typing import Optional

from src.domain.entities.base_entity import BaseEntity
from src.domain.entities.combo_entity import ComboEntity
from src.domain.enums.order_status_enum import OrderStatusEnum
from src.domain.enums.production_status_enum import ProductionStatusEnum


class OrderEntity(BaseEntity):
    combos: list[ComboEntity] = []
    status: OrderStatusEnum = OrderStatusEnum.RECEIVED
    status_production: ProductionStatusEnum = ProductionStatusEnum.PREPARANDO_LANCHE
    start_time: datetime
    finished_time: Optional[datetime] = None