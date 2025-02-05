from pydantic import BaseModel

from src.domain.entities.addon_entity import AddonEntity
from src.domain.entities.product_entity import ProductEntity


class CreateComboDto(BaseModel):
    product: ProductEntity
    addons: list[AddonEntity]