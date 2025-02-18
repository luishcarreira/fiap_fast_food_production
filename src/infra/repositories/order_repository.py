from typing import Callable, AsyncGenerator, Optional

import inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.combo_entity import ComboEntity
from src.domain.entities.order_entity import OrderEntity
from src.domain.enums.production_status_enum import ProductionStatusEnum
from src.domain.interfaces.repositories.i_order_repository import IOrderRepository
from src.infra.models.combo_model import ComboModel
from src.infra.models.order_model import OrderModel


class OrderRepository(IOrderRepository):
    @inject.autoparams()
    def __init__(self, session_factory: Callable[[], AsyncGenerator[AsyncSession, None]]):
        self._session_factory = session_factory

    async def get(self, id_order: int) -> Optional[OrderEntity]:
        try:
            session = await self._session_factory()  # Agora garantimos que session seja AsyncSession
            async with session as s:  # Usamos um alias para evitar sombra de variável
                result = await s.execute(select(OrderModel).filter(OrderModel.id == id_order))
                order_model = await result.scalar_one_or_none()

                if order_model:
                    return OrderEntity(
                        id=order_model.id,
                        status=order_model.status,
                        status_production=order_model.status_production,
                        start_time=order_model.start_time,
                        finished_time=order_model.finished_time,
                        combos=order_model.combos if order_model.combos else [],
                    )

                return None
        except Exception as e:
            raise ValueError(f"Erro ao buscar order: {e}")

    async def create(self, order: OrderEntity) -> Optional[OrderEntity]:
        session = await self._session_factory()
        async with session as s:
            combos_model = []
            for combo in order.combos:
                combo_model = await s.execute(select(ComboModel).filter(ComboModel.id == combo.id))
                if not combo_model.scalar_one_or_none():
                    raise ValueError("Erro! Combo nao encontrado")

                combo_model = await combo_model.scalar_one_or_none()
                combos_model.append(combo_model) if combo_model else None

            order_model = OrderModel(
                status=order.status,
                status_production=order.status_production,
                start_time=order.start_time,
                finished_time=order.finished_time,
                combos=combos_model
            )

            s.add(order_model)
            await s.commit()

            return OrderEntity(
                id=order_model.id,
                status=order_model.status,
                start_time=order_model.start_time,
                finished_time=order_model.finished_time,
                combos=[
                    ComboEntity(
                        id=combo.id,
                        id_product=combo.id_product,
                        addons=combo.addons
                    )
                    for combo in order_model.combos
                ]
            )

    async def update_status(self, id_order: int, status: ProductionStatusEnum) -> Optional[bool]:
        session = await self._session_factory()
        async with session as s:
            result = await s.execute(select(OrderModel).filter(OrderModel.id == id_order))
            order_model = await result.scalar_one_or_none()
            if not order_model:
                return False

            order_model.status_production = status

            await s.commit()

            return True
