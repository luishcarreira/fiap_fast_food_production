import inject

from src.domain.interfaces.services.queue.i_queue_service import IQueueService
from src.domain.usecases.order.dtos.create_order_dto import CreateOrderDto


class SendOrderToQueueUC:
    def __init__(self):
        self.queue_service = inject.instance(IQueueService)

    async def execute(self, order: CreateOrderDto) -> None:
        try:
            await self.queue_service().send_message(
                message=order.model_dump_json()
            )
        except Exception as e:
            print(f"Erro ao enviar pedido para a fila: {str(e)}")
            raise RuntimeError(f"Erro ao enviar pedido para a fila: {str(e)}")
