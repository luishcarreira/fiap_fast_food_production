from pydantic import BaseModel

from src.domain.enums.product_category_enum import ProductCategoryEnum


class CreateAddonDto(BaseModel):
    id: int
    name: str
    price: float
    product_category: ProductCategoryEnum
    discount_percent: float