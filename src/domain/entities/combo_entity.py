from typing import Optional

from src.domain.entities.addon_entity import AddonEntity
from src.domain.entities.base_entity import BaseEntity
from src.domain.entities.product_entity import ProductEntity


class ComboEntity(BaseEntity):
    id_product: int = 0
    addons: list[AddonEntity] = []
    price: Optional[float] = None

    # Nested Objects
    product: ProductEntity | None = None