from typing import Optional, Callable, AsyncGenerator

import inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.addon_entity import AddonEntity
from src.domain.interfaces.repositories.i_addon_repository import IAddonRepository
from src.infra.models.addon_model import AddonModel
from src.infra.utils.generic_mapper import GenericMapper


class AddonRepository(IAddonRepository):
    @inject.autoparams()
    def __init__(self, session_factory: Callable[[], AsyncGenerator[AsyncSession, None]]):
        self._session_factory = session_factory

    async def get(self, id_addon: int) -> Optional[AddonEntity]:
        async for session in self._session_factory():
            result = await session.execute(
                select(AddonModel).filter(AddonModel.id == id_addon)
            )

            addon_model = result.scalars().first()

            return GenericMapper.to_entity(addon_model, AddonEntity) if addon_model else None

    async def create(self, addon_entity: AddonEntity) -> Optional[AddonEntity]:
        async for session in self._session_factory():
            addon_model = GenericMapper.to_model(addon_entity, AddonModel)
            session.add(addon_model)
            await session.commit()

            return GenericMapper.to_entity(addon_model, AddonEntity)
