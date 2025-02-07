from pydantic import BaseModel

from src.domain.enums.product_category_enum import ProductCategoryEnum


class CreateProductDto(BaseModel):
    name: str
    description: str
    price: float
    discount_percent: float
    estimated_time: int
    product_category: ProductCategoryEnum