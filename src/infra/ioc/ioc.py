import inject
from inject import Binder

# sqlalchemy
from src.infra.db.session import get_session

# repositories


class Ioc:

    @staticmethod
    def initialize():
        inject.configure(config=Ioc.config, once=True)

    @staticmethod
    def config(binder: Binder):
        binder.bind("session", get_session)

