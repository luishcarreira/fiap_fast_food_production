from typing import Callable, AsyncGenerator, Optional

import inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.product_entity import ProductEntity
from src.domain.interfaces.repositories.i_product_repository import IProductRepository

from src.infra.models.product_model import ProductModel


class ProductRepository(IProductRepository):
    inject.autoparams()
    def __init__(self, session_provider: Callable[[], AsyncGenerator[AsyncSession, None]]):
        self._session_provider = session_provider

    async def get(self, product_id: int) -> ProductEntity | None:
        try:
            async for session in self._session_provider():
                result = await session.execute(select(ProductModel).where(ProductModel.id == product_id))
                product_model = result.scalar_one_or_none()
                if product_model:
                    product_entity = ProductEntity(
                        id=product_model.id,
                        name=product_model.name,
                        description=product_model.description,
                        estimated_time=product_model.estimated_time,
                        product_category=product_model.product_category
                    )
                    return product_entity
                return None
        except Exception as e:
            raise ValueError(f"Erro ao buscar produto: {e}")

    async def create(self, product_entity: ProductEntity) -> Optional[ProductEntity]:
        async for session in self._session_provider():
            product_model = ProductModel(
                id=product_entity.id,
                name=product_entity.name,
                description=product_entity.description,
                estimated_time=product_entity.estimated_time,
                product_category=product_entity.product_category
            )

            session.add(product_model)
            await session.commit()

            return ProductEntity(
                id=product_model.id,
                name=product_model.name,
                description=product_model.description,
                estimated_time=product_model.estimated_time,
                product_category=product_model.product_category
            )
