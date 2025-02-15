import inject

from src.domain.interfaces.repositories.i_addon_repository import IAddonRepository
from src.domain.interfaces.repositories.i_combo_repository import IComboRepository
from src.domain.interfaces.repositories.i_order_repository import IOrderRepository
from src.domain.interfaces.repositories.i_product_repository import IProductRepository


class BaseUC:
    @inject.autoparams()
    def __init__(self,
                 order_repository: IOrderRepository,
                 combo_repository: IComboRepository,
                 product_repository: IProductRepository,
                 addon_repository: IAddonRepository):
        self._order_repository = order_repository
        self._combo_repository = combo_repository
        self._product_repository = product_repository
        self._addon_repository = addon_repository