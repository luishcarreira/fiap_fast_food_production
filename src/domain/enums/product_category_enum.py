from enum import Enum


class ProductCategoryEnum(str, Enum):
    LANCHE = "Lanche"
    ACOMPANHAMENTO = "Acompanhamento"
    BEBIDA = "Bebida"
    SOBREMESA = "Sobremesa"