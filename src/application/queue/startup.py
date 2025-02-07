from src.application.queue.ioc.ioc import Ioc as IocQueue


class Startup:

    @staticmethod
    def initialize():
        IocQueue.initialize()