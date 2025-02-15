import inject
from inject import Binder, instance

from typing import AsyncGenerator, Callable

from settings import get_settings, Settings
from src.domain.interfaces.repositories.i_addon_repository import IAddonRepository
from src.domain.interfaces.repositories.i_combo_repository import IComboRepository
from src.domain.interfaces.repositories.i_order_repository import IOrderRepository
from src.domain.interfaces.repositories.i_product_repository import IProductRepository
from src.domain.interfaces.services.queue.i_queue_service import IQueueService
from src.infra.db.session import get_session

from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.repositories.addon_repository import AddonRepository
from src.infra.repositories.combo_repository import ComboRepository
from src.infra.repositories.order_repository import OrderRepository
from src.infra.repositories.product_repository import ProductRepository
from src.infra.services.sqs_queue_service.sqs_queue_service import AwsSqsQueueService


class Ioc:
    settings = get_settings()

    @staticmethod
    def initialize():
        inject.configure(config=Ioc.config, once=True)

    @staticmethod
    def config(binder: Binder):
        binder.bind(Settings, Ioc.settings)

        binder.bind(Callable[[], AsyncGenerator[AsyncSession, None]], get_session)

        binder.bind_to_provider(IQueueService, lambda: AwsSqsQueueService(Ioc.settings))

        binder.bind(IOrderRepository, OrderRepository)
        binder.bind(IComboRepository, ComboRepository)
        binder.bind(IProductRepository, ProductRepository)
        binder.bind(IAddonRepository, AddonRepository)
