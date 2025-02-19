from typing import Optional, Callable, AsyncGenerator

import inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.addon_entity import AddonEntity
from src.domain.entities.combo_entity import ComboEntity
from src.domain.interfaces.repositories.i_combo_repository import IComboRepository
from src.infra.models.addon_model import AddonModel
from src.infra.models.combo_model import ComboModel


class ComboRepository(IComboRepository):
    @inject.autoparams()
    def __init__(self, session_factory: Callable[[], AsyncGenerator[AsyncSession, None]]):
        self._session_factory = session_factory

    async def get(self, id_combo: int) -> Optional[ComboEntity]:
        async for session in self._session_factory():
            result = await session.execute(
                select(ComboModel).filter(ComboModel.id == id_combo)
            )
            combo_model = result.scalars().first()
            if combo_model:

                combo_entity = ComboEntity(
                    id=combo_model.id,
                    id_product=combo_model.id_product,
                    addons=[AddonEntity(id=addon.id, name=addon.name, product_category=addon.product_category) for addon in combo_model.addons],
                )
                return combo_entity
            return None

    async def create(self, combo_entity: ComboEntity) -> Optional[ComboEntity]:
        async for session in self._session_factory():
            combo_model = ComboModel(
                id=combo_entity.id,
                id_product=combo_entity.id_product,
            )

            addon_ids = [addon.id for addon in combo_entity.addons]
            addons = await session.execute(
                select(AddonModel).filter(AddonModel.id.in_(addon_ids))
            )
            addon_list = addons.scalars().all()

            # Associate addons with combo
            combo_model.addons.extend(addon_list)

            session.add(combo_model)
            await session.commit()
            await session.refresh(combo_model)

            return ComboEntity(
                id=combo_model.id,
                id_product=combo_model.id_product,
                addons=[AddonEntity(id=addon.id, name=addon.name, product_category=addon.product_category) for addon in combo_model.addons],
            )