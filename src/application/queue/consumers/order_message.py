from src.domain.entities.order_entity import OrderEntity
from src.domain.interfaces.services.queue.i_message import IMessage, MessagePriority, T


class OrderMessage(IMessage):
    @property
    def content(self) -> T:
        return OrderEntity

    @property
    def priority(self) -> MessagePriority:
        return MessagePriority.MEDIUM
