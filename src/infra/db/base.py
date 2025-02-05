
import enum
from sqlalchemy import Enum
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    type_annotation_map = {
        enum.Enum: Enum(enum.Enum, native_enum=False),
    }

from src.infra.models.addon_model import AddonModel
from src.infra.models.combo_model import ComboModel
from src.infra.models.product_model import ProductModel
# from src.infra.models.order_model import OrderModel