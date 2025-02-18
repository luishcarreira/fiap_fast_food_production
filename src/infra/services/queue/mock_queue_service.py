import asyncio
from typing import Any, List
from src.domain.interfaces.services.queue.i_queue_service import IQueueService


class MockQueueService(IQueueService):
    sent_messages = []
    received_messages = []

    async def send_message(self, message: Any, delay_seconds: int = 0) -> None:
        """Simula o envio de uma mensagem para a fila"""
        print(f"Mock sending message to queue: {message}")
        # Adiciona a mensagem à lista de mensagens enviadas
        self.sent_messages.append(message)
        # Simula um delay para comportamento assíncrono
        if delay_seconds > 0:
            await asyncio.sleep(delay_seconds)

    async def receive_messages(self, max_messages: int = 10) -> List[str]:
        """Simula o recebimento de mensagens da fila"""
        # Retorna as mensagens "enviadas" até o momento, respeitando o limite de max_messages
        return self.received_messages[:max_messages]

    def add_message_to_receive(self, message: Any) -> None:
        """Adiciona uma mensagem à lista de mensagens recebidas, para simular o recebimento"""
        self.received_messages.append(message)

    def clear_queue(self):
        """Limpa as mensagens enviadas para que o teste comece com a fila vazia"""
        self.sent_messages.clear()