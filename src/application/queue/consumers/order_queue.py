from src.application.queue.consumers.order_message import OrderMessage
from src.domain.interfaces.services.queue.i_queue_handler import IQueueHandler


class OrderConsumer(IQueueHandler):
    async def handle_message(self, message: OrderMessage) -> None:
        print(f"Processando mensagem: {message.content}")