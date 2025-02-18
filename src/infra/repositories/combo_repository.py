from typing import Optional, Callable, AsyncGenerator

import inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.combo_entity import ComboEntity
from src.domain.interfaces.repositories.i_combo_repository import IComboRepository
from src.infra.models.combo_model import ComboModel
from src.infra.utils.generic_mapper import GenericMapper


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
                    price=combo_model.price,
                    addons=combo_model.addons,
                )
                return combo_entity
            return None

    async def create(self, combo_entity: ComboEntity) -> Optional[ComboEntity]:
        async for session in self._session_factory():
            combo_model = ComboModel(
                id_product=combo_entity.id_product,
                price=combo_entity.price,
                addons=combo_entity.addons
            )
            session.add(combo_model)
            await session.commit()

            return ComboEntity(
                id=combo_model.id,
                id_product=combo_model.id_product,
                price=combo_model.price,
                addons=combo_model.addons
            )
