from pydantic import BaseModel

from src.domain.enums.product_category_enum import ProductCategoryEnum


class CreateProductDto(BaseModel):
    id: int
    name: str
    description: str
    estimated_time: int
    product_category: ProductCategoryEnum