
import inject
from inject import Binder

from typing import Callable, AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession
from src.infra.db.session import get_session

from src.domain.interfaces.repositories.i_product_repository import IProductRepository
from src.domain.interfaces.services.queue.i_queue_service import IQueueService

from src.domain.interfaces.repositories.i_order_repository import IOrderRepository
from src.infra.repositories.order_repository import OrderRepository
from src.infra.repositories.product_repository import ProductRepository

from src.infra.services.sqs_queue_service.sqs_queue_service import AwsSqsQueueService


class Ioc:

    @staticmethod
    def initialize():
        inject.configure(config=Ioc.config, once=True)

    @staticmethod
    def config(binder: Binder):
        binder.bind(Callable[[], AsyncGenerator[AsyncSession, None]], get_session)

        binder.bind(IQueueService, AwsSqsQueueService())

        binder.bind(IOrderRepository, OrderRepository)
        binder.bind(IProductRepository, ProductRepository)
