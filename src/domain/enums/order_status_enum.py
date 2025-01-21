from enum import Enum


class OrderStatusEnum(str, Enum):
    RECEIVED = "Received"
    IN_PREPARATION = "In preparation"
    READY = "Ready"
    FINALIZED = "Finalized"