from enum import Enum


class ProductCategoryEnum(str, Enum):
    LANCHE = "Lanche"
    ACOMPANHAMENTO = "Acompanhamento"
    BEBIDAS = "Bebidas"
    SOBREMESA = "Sobremesa"