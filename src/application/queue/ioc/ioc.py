import inject
from inject import Binder


from src.domain.interfaces.repositories.i_addon_repository import IAddonRepository
from src.domain.interfaces.repositories.i_combo_repository import IComboRepository
from src.domain.interfaces.repositories.i_order_repository import IOrderRepository
from src.domain.interfaces.repositories.i_product_repository import IProductRepository
from src.domain.interfaces.services.queue.i_queue_service import IQueueService

from src.infra.repositories.addon_repository import AddonRepository
from src.infra.repositories.combo_repository import ComboRepository
from src.infra.repositories.order_repository import OrderRepository
from src.infra.repositories.product_repository import ProductRepository
from src.infra.services.queue.sqs_queue_service import AwsSqsQueueService


class Ioc:

    @staticmethod
    def initialize():
        inject.configure(config=Ioc.config, once=True)

    @staticmethod
    def config(binder: Binder):
        binder.bind_to_provider(IQueueService, lambda: AwsSqsQueueService())

        binder.bind(IOrderRepository, OrderRepository)
        binder.bind(IComboRepository, ComboRepository)
        binder.bind(IProductRepository, ProductRepository)
        binder.bind(IAddonRepository, AddonRepository)
