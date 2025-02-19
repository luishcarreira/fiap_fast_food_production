from src.domain.usecases.common.base_uc import BaseUC


class OrderGetAllUC(BaseUC):

    async def execute(self):
        return await self._order_repository.get_all()