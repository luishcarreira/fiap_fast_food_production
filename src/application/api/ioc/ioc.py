
import inject
from inject import Binder

from typing import Callable, AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from settings import Settings, get_settings
from src.infra.db.session import get_session

from src.domain.interfaces.services.queue.i_queue_service import IQueueService

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
