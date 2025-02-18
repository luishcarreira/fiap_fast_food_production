from src.domain.entities.base_entity import BaseEntity
from src.domain.enums.product_category_enum import ProductCategoryEnum


class AddonEntity(BaseEntity):
    name: str
    product_category: ProductCategoryEnum