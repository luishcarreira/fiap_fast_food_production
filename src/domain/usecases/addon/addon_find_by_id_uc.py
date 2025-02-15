from src.domain.usecases.common.base_uc import BaseUC


class AddonFindByIdUC(BaseUC):

    async def execute(self, id_addon: int) -> AddonEntity or None:
        if not id_addon:
            raise Exception("O id do addon eh obrigatorio")

        return await self._addon_repository.get(id_addon)
