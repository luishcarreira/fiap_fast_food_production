from __future__ import annotations

from src.infra.db.base import Base

from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column

combo_addon_association = Table(
    "combo_addon",
    Base.metadata,
    Column("combo_id", Integer, ForeignKey("combos.id"), primary_key=True),
    Column("addon_id", Integer, ForeignKey("addons.id"), primary_key=True),
)


class ComboModel(Base):
    __tablename__ = "combos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_product: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)

    product: Mapped["ProductModel"] = relationship("ProductModel", back_populates="combos")
    addons: Mapped[list["AddonModel"]] = relationship(secondary=combo_addon_association, back_populates="combos")
    order: Mapped["OrderModel"] = relationship("OrderModel", back_populates="combos")
