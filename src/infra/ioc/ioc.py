from typing import AsyncGenerator, Callable

import inject
from inject import Binder

# sqlalchemy
from src.infra.db.session import get_session
from sqlalchemy.ext.asyncio import AsyncSession

# interfaces
from src.domain.interfaces.i_order_repository import IOrderRepository

# repositories
from src.infra.repositories.order_repository import OrderRepository

# usecases
from src.domain.usecases.product.product_find_by_id_uc import ProductFindByIdUC


class Ioc:

    @staticmethod
    def initialize():
        inject.configure(config=Ioc.config, once=True)

    @staticmethod
    def config(binder: Binder):
        binder.bind(Callable[[], AsyncGenerator[AsyncSession, None]], get_session)

        binder.bind(IOrderRepository, OrderRepository)

        binder.bind("product_find_by_id_uc", ProductFindByIdUC)
