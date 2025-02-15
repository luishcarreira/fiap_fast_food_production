from abc import ABC, abstractmethod
from typing import Any, List


class IQueueService(ABC):

    @abstractmethod
    async def send_message(self, message: Any, delay_seconds: int = 0) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def receive_messages(self, max_messages: int = 10) -> List[str]:
        raise NotImplementedError()
