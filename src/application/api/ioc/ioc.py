
import inject
from inject import Binder

from typing import Callable, AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from settings import Settings, get_settings
from src.infra.db.session import get_session

from src.domain.interfaces.services.queue.i_queue_service import IQueueService

from src.infra.services.sqs_queue_service.sqs_queue_service import AwsSqsQueueService

from src.domain.interfaces.repositories.i_addon_repository import IAddonRepository
from src.domain.interfaces.repositories.i_combo_repository import IComboRepository
from src.domain.interfaces.repositories.i_order_repository import IOrderRepository
from src.domain.interfaces.repositories.i_product_repository import IProductRepository
from src.infra.repositories.addon_repository import AddonRepository
from src.infra.repositories.combo_repository import ComboRepository
from src.infra.repositories.order_repository import OrderRepository
from src.infra.repositories.product_repository import ProductRepository

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

        binder.bind(IOrderRepository, OrderRepository(get_session))
        binder.bind(IComboRepository, ComboRepository(get_session))
        binder.bind(IProductRepository, ProductRepository(get_session))
        binder.bind(IAddonRepository, AddonRepository(get_session))
