from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from enum import Enum


class MessagePriority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


T = TypeVar("T")


class IMessage(ABC, Generic[T]):
    @property
    @abstractmethod
    def content(self) -> T:
        raise NotImplementedError()

    @property
    @abstractmethod
    def priority(self) -> MessagePriority:
        raise NotImplementedError()
