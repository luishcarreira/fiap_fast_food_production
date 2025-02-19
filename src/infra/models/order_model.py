from __future__ import annotations

from datetime import datetime

from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.domain.enums.order_status_enum import OrderStatusEnum
from src.domain.enums.production_status_enum import ProductionStatusEnum
from src.infra.db.base import Base
from src.infra.models.combo_model import ComboModel


class OrderModel(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    status: Mapped[OrderStatusEnum] = mapped_column(default=OrderStatusEnum.RECEIVED.value)
    status_production: Mapped[ProductionStatusEnum] = mapped_column(default=ProductionStatusEnum.PREPARANDO_LANCHE.value)
    start_time: Mapped[datetime] = mapped_column(nullable=False)
    finished_time: Mapped[datetime] = mapped_column(nullable=True)

    combos: Mapped[list["ComboModel"]] = relationship("ComboModel", back_populates="order", foreign_keys="ComboModel.id_order", lazy="joined")
