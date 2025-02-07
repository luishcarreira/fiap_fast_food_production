from abc import ABC, abstractmethod
from typing import Any


class IQueueHandler(ABC):
    @abstractmethod
    async def handle_message(self, message: Any) -> None:
        raise NotImplementedError()