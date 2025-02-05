from pydantic import BaseModel


class FindByIdProductDto(BaseModel):
    id: int