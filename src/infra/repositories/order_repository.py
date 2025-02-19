from typing import Callable, AsyncGenerator, Optional

import inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.addon_entity import AddonEntity
from src.domain.entities.combo_entity import ComboEntity
from src.domain.entities.order_entity import OrderEntity
from src.domain.enums.production_status_enum import ProductionStatusEnum
from src.domain.interfaces.repositories.i_order_repository import IOrderRepository
from src.infra.models.addon_model import AddonModel
from src.infra.models.combo_model import ComboModel
from src.infra.models.order_model import OrderModel


class OrderRepository(IOrderRepository):

    @inject.autoparams()
    def __init__(self, session_factory: Callable[[], AsyncGenerator[AsyncSession, None]]):
        self._session_factory = session_factory

    async def get_all(self) -> Optional[OrderEntity]:
        try:
            async for session in self._session_factory():  # Usamos um alias para evitar sombra de variável
                result = await session.execute(select(OrderModel))
                order_model = result.scalars().all()

                if order_model:
                    return [
                        OrderEntity(
                            id=order.id,
                            status=order.status,
                            status_production=order.status_production,
                            start_time=order.start_time,
                            finished_time=order.finished_time,
                            combos=[
                                ComboEntity(
                                    id=combo.id,
                                    id_product=combo.id_product,
                                    addons=[
                                        AddonEntity(
                                            id=addon.id,
                                            name=addon.name,
                                            product_category=addon.product_category
                                        )
                                        for addon in combo.addons
                                    ]
                                )
                                for combo in order.combos
                            ]
                        )
                        for order in order_model
                    ]

                return None
        except Exception as e:
            raise ValueError(f"Erro ao buscar order: {e}")

    async def get(self, id_order: int) -> Optional[OrderEntity]:
        try:
            async for session in self._session_factory():  # Usamos um alias para evitar sombra de variável
                result = await session.execute(select(OrderModel).filter(OrderModel.id == id_order))
                order_model = result.scalar_one_or_none()

                if order_model:
                    return OrderEntity(
                        id=order_model.id,
                        status=order_model.status,
                        status_production=order_model.status_production,
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

                return None
        except Exception as e:
            raise ValueError(f"Erro ao buscar order: {e}")

    async def create(self, order: OrderEntity) -> Optional[OrderEntity]:
        async for session in self._session_factory():
            order_model = OrderModel(
                status=order.status,
                status_production=order.status_production,
                start_time=order.start_time,
                finished_time=order.finished_time,
            )

            combo_ids = [combo.id for combo in order.combos]
            combos = await session.execute(
                select(ComboModel).filter(ComboModel.id.in_(combo_ids))
            )
            combo_list = combos.scalars().all()

            # Associate combos with order
            order_model.combos.extend(combo_list)

            session.add(order_model)
            await session.commit()
            await session.refresh(order_model)

            return OrderEntity(
                id=order_model.id,
                status=order_model.status,
                start_time=order_model.start_time,
                finished_time=order_model.finished_time,
                combos=[
                    ComboEntity(
                        id=combo.id,
                        id_product=combo.id_product,
                        addons=[
                            AddonEntity(
                                id=addon.id,
                                name=addon.name,
                                product_category=addon.product_category
                            )
                            for addon in combo.addons
                        ]
                    )
                    for combo in order_model.combos
                ]
            )

    async def update_status(self, id_order: int, status: ProductionStatusEnum) -> Optional[bool]:
        async for session in self._session_factory():
            result = await session.execute(select(OrderModel).filter(OrderModel.id == id_order))
            order_model = result.scalar_one_or_none()
            if not order_model:
                return False

            order_model.status_production = status

            await session.commit()

            return True
