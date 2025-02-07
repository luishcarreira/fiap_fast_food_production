from pydantic import BaseModel

from src.domain.usecases.addon.dtos.create_addon_dto import CreateAddonDto
from src.domain.usecases.product.dtos.create_product_dto import CreateProductDto


class CreateComboDto(BaseModel):
    product: CreateProductDto
    addons: list[CreateAddonDto]