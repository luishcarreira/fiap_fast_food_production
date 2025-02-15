from datetime import datetime

from src.domain.entities.addon_entity import AddonEntity
from src.domain.entities.combo_entity import ComboEntity
from src.domain.entities.order_entity import OrderEntity
from src.domain.entities.product_entity import ProductEntity
from src.domain.enums.order_status_enum import OrderStatusEnum

from src.domain.usecases.common.base_uc import BaseUC

from src.domain.usecases.order.dtos.create_order_dto import CreateOrderDto


class OrderCreateUC(BaseUC):
    async def execute(self, create_order_dto: CreateOrderDto) -> OrderEntity:
        if not create_order_dto:
            raise ValueError("Erro! O pedido eh obrigatorio")

        if not create_order_dto.combos:
            raise ValueError("Erro! O pedido deve conter pelo menos um combo")

        list_combos: list[ComboEntity] = []
        for combo in create_order_dto.combos:
            combo_entity = await self._process_combo(combo)

            await self._combo_repository.create(combo_entity)

            list_combos.append(combo_entity)

        order_entity = OrderEntity(
            id=create_order_dto.id,
            combos=list_combos,
            status=OrderStatusEnum.RECEIVED,
            start_time=datetime.now(),
            u_inserted=1,  # mock
            inserted=datetime.now()
        )

        return await self._order_repository.create(order_entity)

    async def _process_combo(self, combo) -> ComboEntity:
        combo_entity = ComboEntity(
            u_inserted=1, # mock
            inserted=datetime.now(),
            id_product=0
        )

        product = await self._get_product(combo.product.id)

        if not product:
            product = await self._create_product(ProductEntity(**combo.product.model_dump(exclude_none=True)))

        combo_entity.id_product = product.id

        for addon in combo.addons:
            addon_entity = await self._get_addon(addon.id)

            if not addon_entity:
                addon_entity = await self._create_addon(AddonEntity(**addon.model_dump(exclude_none=True)))

            combo_entity.addons.append(addon_entity)

        return combo_entity

    async def _get_product(self, product_id: int) -> ProductEntity | None:
        if not product_id:
            raise ValueError("Erro! O id do produto eh obrigatorio")

        return await self._product_repository.get(product_id)

    async def _create_product(self, product_entity: ProductEntity) -> ProductEntity:
        product_created = await self._product_repository.create(product_entity)

        if not product_created:
            raise ValueError("Erro ao cadastrar produto")

        return product_created

    async def _get_addon(self, addon_id: int) -> AddonEntity | None:
        if not addon_id:
            raise ValueError("Erro! O id do addon eh obrigatorio")

        return await self._addon_repository.get(addon_id)

    async def _create_addon(self, addon_entity: AddonEntity) -> AddonEntity:
        addon_created = await self._addon_repository.create(addon_entity)

        if not addon_created:
            raise ValueError("Erro ao cadastrar addon")

        return addon_created