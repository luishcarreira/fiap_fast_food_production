from typing import Callable, AsyncGenerator

import inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.product_entity import ProductEntity
from src.domain.interfaces.i_product_repository import IProductRepository

from src.infra.models.product_model import ProductModel
from src.infra.utils.generic_mapper import GenericMapper


class ProductRepository(IProductRepository):
    @inject.autoparams()
    def __init__(self, session_factory: Callable[[], AsyncGenerator[AsyncSession, None]]):
        self._session_factory = session_factory

    async def get(self, product_id: int) -> ProductEntity | None:
        async for session in self._session_factory():
            result = await session.execute(
                select(ProductModel).filter(ProductModel.id == product_id)
            )

            product_model = result.scalars().first()

            return GenericMapper.to_entity(product_model, ProductEntity) if product_model else None

        return None
