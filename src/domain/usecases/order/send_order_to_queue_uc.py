import inject

from src.domain.interfaces.services.queue.i_queue_service import IQueueService
from src.domain.usecases.order.dtos.create_order_dto import CreateOrderDto


class SendOrderToQueueUC:
    @inject.autoparams()
    def __init__(self, queue_service: IQueueService):
        self.queue_service = queue_service

    async def execute(self, order: CreateOrderDto) -> None:
        try:
            await self.queue_service.send_message(
                message=order.model_dump_json()
            )
        except Exception as e:
            raise RuntimeError(f"Erro ao enviar pedido para a fila: {str(e)}")
