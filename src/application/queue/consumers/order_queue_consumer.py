import json

from src.domain.interfaces.services.queue.i_queue_handler import IQueueHandler
from src.domain.usecases.order.dtos.create_order_dto import CreateOrderDto
from src.domain.usecases.order.order_create_uc import OrderCreateUC


class OrderQueueConsumer(IQueueHandler):
    async def handle_message(self, message: str) -> None:
        if not message:
            raise ValueError("Mensagem vazia")

        create_order_dto = CreateOrderDto(**json.loads(message))

        await OrderCreateUC().execute(create_order_dto)