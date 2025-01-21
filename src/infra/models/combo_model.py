from sqlalchemy import Column, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from src.infra.db.base import Base

combo_addon_association = Table(
    "combo_addon",
    Base.metadata,
    Column("combo_id", Integer, ForeignKey("combos.id"), primary_key=True),
    Column("addon_id", Integer, ForeignKey("addons.id"), primary_key=True),
)

class ComboModel(Base):
    __tablename__ = "combos"

    id = Column(Integer, primary_key=True, index=True)
    id_product = Column(Integer, ForeignKey("products.id"), nullable=False)
    price = Column(Float, nullable=False)

    # Relacionamentos
    product = relationship("ProductModel", back_populates="combos")
    addons = relationship("AddonModel", secondary=combo_addon_association, back_populates="combos")

    order = relationship("OrderModel", back_populates="combos")
