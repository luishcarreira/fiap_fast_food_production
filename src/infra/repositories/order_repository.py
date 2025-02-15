from typing import Callable, AsyncGenerator, Optional

import inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.order_entity import OrderEntity
from src.domain.interfaces.repositories.i_order_repository import IOrderRepository
from src.infra.models.order_model import OrderModel
from src.infra.utils.generic_mapper import GenericMapper


class OrderRepository(IOrderRepository):
    @inject.autoparams()
    def __init__(self, session_factory: Callable[[], AsyncGenerator[AsyncSession, None]]):
        self._session_factory = session_factory

    async def get(self, order_id: int) -> Optional[OrderEntity]:
        async for session in self._session_factory():
            result = await session.execute(
                select(OrderModel).filter(OrderModel.id == order_id)
            )

            order_model = result.scalars().first()

            return GenericMapper.to_entity(order_model, OrderEntity) if order_model else None

    async def create(self, order: OrderEntity) -> Optional[OrderEntity]:
        pass

    async def update(self, order: OrderEntity) -> Optional[OrderEntity]:
        pass
