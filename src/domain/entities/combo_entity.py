from src.domain.entities.addon_entity import AddonEntity
from src.domain.entities.base_entity import BaseEntity
from src.domain.entities.product_entity import ProductEntity


class ComboEntity(BaseEntity):
    id_product: int
    addons: list[AddonEntity]
    price: float

    # Nested Objects
    product: ProductEntity | None = None