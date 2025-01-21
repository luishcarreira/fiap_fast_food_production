from src.domain.entities.base_entity import BaseEntity
from src.domain.enums.product_category_enum import ProductCategoryEnum


class ProductEntity(BaseEntity):
    name: str
    description: str
    price: float
    discount_percent: float
    estimated_time: int
    product_category: ProductCategoryEnum