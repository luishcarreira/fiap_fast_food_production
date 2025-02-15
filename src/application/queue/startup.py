import asyncio

from src.application.queue import start_consumer
from src.application.queue.ioc.ioc import Ioc as IocQueue


class Startup:

    @staticmethod
    def initialize():
        IocQueue.initialize()

        asyncio.run(start_consumer())