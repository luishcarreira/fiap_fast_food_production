from src.domain.entities.base_entity import BaseEntity


class CustomerEntity(BaseEntity):
    name: str
    cpf: str
    email: str