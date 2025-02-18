from typing_extensions import Optional

from src.domain.enums.order_status_enum import OrderStatusEnum
from src.domain.enums.production_status_enum import ProductionStatusEnum
from src.domain.usecases.common.base_uc import BaseUC
from src.infra.services.order_api.order_api import OrderApi


async def _update_status_order_api(id_order: int, status: OrderStatusEnum) -> Optional[bool]:
    result = await OrderApi().update_status_order(id_order, status.value)
    return result


class OrderUpdateStatusUC(BaseUC):
    async def execute(self, id_order: int, status: ProductionStatusEnum):
        if id_order is None or 0:
            raise ValueError("Invalid id order")

        if status is None:
            raise ValueError("Invalid status")

        order = await self._order_repository.get(id_order)

        if not order:
            raise ValueError("Order not found")

        if status == ProductionStatusEnum.FINALIZADO:
            await _update_status_order_api(id_order, OrderStatusEnum.READY)

        order.status_production = status

        return await self._order_repository.update_status(order.id, status)
