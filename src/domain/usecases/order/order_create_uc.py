from datetime import datetime

import inject

from src.domain.entities.order_entity import OrderEntity
from src.domain.entities.product_entity import ProductEntity
from src.domain.interfaces.i_order_repository import IOrderRepository
from src.domain.usecases.order.dtos.create_order_dto import CreteOrderDto


class OrderCreateUC:
    @inject.autoparams()
    def __init__(self, order_repo: IOrderRepository):
        self.order_repo = order_repo

    def execute(self, create_order_dto: CreteOrderDto) -> OrderEntity:
        order_entity = OrderEntity(
            start_time=datetime.now(),

            u_inserted=0,
            inserted=datetime.now()
        )

        # get combos


        return self.order_repo.create(order_entity)

    def _get_product(self, product_id: int) -> ProductEntity:
        pass

