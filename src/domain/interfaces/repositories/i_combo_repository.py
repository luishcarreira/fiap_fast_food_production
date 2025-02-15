from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.combo_entity import ComboEntity


class IComboRepository(ABC):

    @abstractmethod
    async def get(self, id_combo: int) -> Optional[ComboEntity]:
        raise NotImplementedError

    @abstractmethod
    async def create(self, combo_entity: ComboEntity) -> Optional[ComboEntity]:
        raise NotImplementedError