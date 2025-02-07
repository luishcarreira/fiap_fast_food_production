import inject
import json

from src.domain.interfaces.services.queue.i_queue_service import IQueueService
from src.domain.usecases.order.dtos.create_order_dto import CreteOrderDto


class SendOrderToQueueUC:
    @inject.autoparams()
    def __init__(self, queue_service: IQueueService):
        self.queue_service = queue_service

    async def execute(self, queue_name: str, order: CreteOrderDto) -> None:
        if not queue_name or not order:
            raise ValueError("O nome da fila e a entidade do pedido são obrigatórios!")

        try:
            await self.queue_service.send_message(
                queue_name=queue_name,
                message=order.model_dump_json()
            )
        except Exception as e:
            raise RuntimeError(f"Erro ao enviar pedido para a fila: {str(e)}")
