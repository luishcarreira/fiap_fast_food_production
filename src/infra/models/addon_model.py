from sqlalchemy import Column, Integer, Float, String, Enum
from sqlalchemy.orm import relationship

from src.infra.db.base import Base
from src.domain.enums.product_category_enum import ProductCategoryEnum
from src.infra.models.combo_model import combo_addon_association


class AddonModel(Base):
    __tablename__ = "addons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    product_category = Column(Enum(ProductCategoryEnum), nullable=False)
    discount_percent = Column(Float, nullable=False)

    combos = relationship(
        "ComboModel", secondary=combo_addon_association, back_populates="addons"
    )