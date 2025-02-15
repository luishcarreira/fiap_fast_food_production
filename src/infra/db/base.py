
import enum
from sqlalchemy import Enum
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    type_annotation_map = {
        enum.Enum: Enum(enum.Enum, native_enum=False),
    }