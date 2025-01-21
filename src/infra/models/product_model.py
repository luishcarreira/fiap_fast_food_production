from sqlalchemy import Column, Integer, Float, String, Enum
from sqlalchemy.orm import relationship
from src.infra.db.base import Base
from src.domain.enums.product_category_enum import ProductCategoryEnum

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    discount_percent = Column(Float, nullable=False)
    estimated_time = Column(Integer, nullable=False)
    product_category = Column(Enum(ProductCategoryEnum), nullable=False)

    # Relacionamentos
    combos = relationship("ComboModel", back_populates="product")
