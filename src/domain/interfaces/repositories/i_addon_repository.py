from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.addon_entity import AddonEntity


class IAddonRepository(ABC):

    @abstractmethod
    async def get(self, id_addon: int) -> Optional[AddonEntity]:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, addon_entity: AddonEntity) -> Optional[AddonEntity]:
        raise NotImplementedError()