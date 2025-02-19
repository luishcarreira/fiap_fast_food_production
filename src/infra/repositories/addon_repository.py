from typing import Optional, Callable, AsyncGenerator

import inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.addon_entity import AddonEntity
from src.domain.interfaces.repositories.i_addon_repository import IAddonRepository
from src.infra.models.addon_model import AddonModel


class AddonRepository(IAddonRepository):
    @inject.autoparams()
    def __init__(self, session_factory: Callable[[], AsyncGenerator[AsyncSession, None]]):
        self._session_factory = session_factory

    async def get(self, id_addon: int) -> Optional[AddonEntity]:
        try:
            async for session in self._session_factory():
                result = await session.execute(select(AddonModel).filter(AddonModel.id == id_addon))
                addon_model = result.scalar_one_or_none()
                if addon_model:
                    addon_entity = AddonEntity(
                        id=addon_model.id,
                        name=addon_model.name,
                        product_category=addon_model.product_category
                    )
                    return addon_entity

                return None
        except Exception as e:
            raise ValueError(f"Erro ao buscar produto: {e}")

    async def create(self, addon_entity: AddonEntity) -> Optional[AddonEntity]:
        async for session in self._session_factory():
            addon_model = AddonModel(
                id=addon_entity.id,
                name=addon_entity.name,
                product_category=addon_entity.product_category
            )

            session.add(addon_model)
            await session.commit()

            return AddonEntity(
                id=addon_model.id,
                name=addon_model.name,
                product_category=addon_model.product_category
            )
