from sqlalchemy import Column, Integer, Float, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.infra.db.base import Base
from src.domain.enums.order_status_enum import OrderStatusEnum

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    total_price = Column(Float, nullable=False)
    status = Column(Enum(OrderStatusEnum), default=OrderStatusEnum.RECEIVED.value)
    finished_time = Column(DateTime, nullable=True)

    # Relações
    id_customer = Column(Integer, ForeignKey("customers.id"), nullable=False)
    customer = relationship("CustomerModel", back_populates="orders")
    combos = relationship("ComboModel", back_populates="order")
