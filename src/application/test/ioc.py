import inject
from inject import Binder

from src.domain.interfaces.services.queue.i_queue_service import IQueueService
from src.infra.services.queue.mock_queue_service import MockQueueService


class Ioc:
    @staticmethod
    def initialize():
        inject.configure(config=Ioc.config, once=True)

    @staticmethod
    def config(binder: Binder):
        binder.bind(IQueueService, MockQueueService)