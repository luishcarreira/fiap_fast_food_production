from __future__ import annotations

from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.infra.db.base import Base
from src.domain.enums.product_category_enum import ProductCategoryEnum
from src.infra.models.combo_model import combo_addon_association, ComboModel


class AddonModel(Base):
    __tablename__ = "addons"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    product_category: Mapped[ProductCategoryEnum] = mapped_column(nullable=False)
    discount_percent: Mapped[float] = mapped_column(nullable=False)

    combos: Mapped[list[ComboModel]] = relationship(
        secondary=combo_addon_association, back_populates="addons"
    )
