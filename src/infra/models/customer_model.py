from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.infra.db.base import Base

class CustomerModel(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    orders = relationship("OrderModel", back_populates="customer")
