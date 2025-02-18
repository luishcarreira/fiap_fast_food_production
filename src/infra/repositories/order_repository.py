from typing import Callable, AsyncGenerator, Optional

import inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.order_entity import OrderEntity
from src.domain.interfaces.repositories.i_order_repository import IOrderRepository
from src.infra.models.combo_model import ComboModel
from src.infra.models.order_model import OrderModel


class OrderRepository(IOrderRepository):
    @inject.autoparams()
    def __init__(self, session_factory: Callable[[], AsyncGenerator[AsyncSession, None]]):
        self._session_factory = session_factory

    async def get(self, order_id: int) -> Optional[OrderEntity]:
        try:
            async for session in self._session_factory():
                result = await session.execute(select(OrderModel).filter(OrderModel.id == order_id))
                order_model = result.scalar_one_or_none()
                if order_model:
                    order_entity = OrderEntity(
                        id=order_model.id,
                        status=order_model.status,
                        start_time=order_model.start_time,
                        finished_time=order_model.finished_time,
                        combos=order_model.combos if order_model.combos else [],
                    )

                    return order_entity

                return None
        except Exception as e:
            raise ValueError(f"Erro ao buscar produto: {e}")

    async def create(self, order: OrderEntity) -> Optional[OrderEntity]:
        async def create(self, order: OrderEntity) -> Optional[OrderEntity]:
            async for session in self._session_factory():
                combos_model = []
                for combo in order.combos:
                    combo_model = await session.execute(select(ComboModel).filter(ComboModel.id == combo.id))
                    if not combo_model.scalar_one_or_none():
                        raise ValueError("Erro! Combo nao encontrado")

                    combo_model = combo_model.scalar_one_or_none()
                    combos_model.append(combo_model)

                order_model = OrderModel(
                    status=order.status,
                    start_time=order.start_time,
                    finished_time=order.finished_time,
                    combos=combos_model
                )

                session.add(order_model)
                await session.commit()

                return OrderEntity(
                    id=order_model.id,
                    status=order_model.status,
                    start_time=order_model.start_time,
                    finished_time=order_model.finished_time,
                    combos=[ComboEntity(id=combo.id, id_product=combo.id_product, price=combo.price, addons=combo.addons) for combo in order_model.combos]
                )

    async def update(self, order: OrderEntity) -> Optional[OrderEntity]:
        try:
            async for session in self._session_factory():
                result = await session.execute(select(OrderModel).filter(OrderModel.id == order.id))
                order_model = result.scalar_one_or_none()
                if order_model:
                    order_model.status = order.status
                    order_model.start_time = order.start_time
                    order_model.finished_time = order.finished_time
                    order_model.combos = order.combos

                    await session.commit()

                    return OrderEntity(
                        id=order_model.id,
                        status=order_model.status,
                        start_time=order_model.start_time,
                        finished_time=order_model.finished_time,
                        combos=order_model.combos if order_model.combos else []
                    )
                return None
        except Exception as e:
            raise ValueError(f"Erro ao atualizar pedido: {e}")
