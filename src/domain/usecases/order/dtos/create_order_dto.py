from pydantic import BaseModel

from src.domain.usecases.combo.dtos.create_combo_dto import CreateComboDto


class CreateOrderDto(BaseModel):
    id: int
    combos: list[CreateComboDto]