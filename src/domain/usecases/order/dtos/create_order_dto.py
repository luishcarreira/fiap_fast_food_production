from pydantic import BaseModel

from src.domain.usecases.combo.dtos.create_combo_dto import CreateComboDto


class CreteOrderDto(BaseModel):
    combos: list[CreateComboDto]