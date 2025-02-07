import inject
from botocore.config import Config
from inject import Binder

from typing import AsyncGenerator, Callable

from settings import get_settings
from src.infra.db.session import get_session

from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.services.sqs_queue_service.sqs_queue_service import AwsSqsQueueService


class Ioc:

    @staticmethod
    def initialize():
        inject.configure(config=Ioc.config, once=True)

    @staticmethod
    def config(binder: Binder):
        binder.bind(Callable[[], AsyncGenerator[AsyncSession, None]], get_session)
