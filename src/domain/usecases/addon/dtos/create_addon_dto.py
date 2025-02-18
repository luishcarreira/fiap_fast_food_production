from pydantic import BaseModel

from src.domain.enums.product_category_enum import ProductCategoryEnum


class CreateAddonDto(BaseModel):
    id: int
    name: str
    product_category: ProductCategoryEnum