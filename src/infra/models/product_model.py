from __future__ import annotations

from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.infra.db.base import Base
from src.domain.enums.product_category_enum import ProductCategoryEnum

from src.infra.models.combo_model import ComboModel


class ProductModel(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    discount_percent: Mapped[float] = mapped_column(nullable=False)
    estimated_time: Mapped[int] = mapped_column(nullable=False)
    product_category: Mapped[ProductCategoryEnum] = mapped_column(nullable=False)

    # Relacionamentos
    combos: Mapped[list[ComboModel]] = relationship(back_populates="product")
