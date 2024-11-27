from enum import Enum

class Categoria(Enum):
    CATEGORIA_1 = 'Categoria1'
    CATEGORIA_2 = 'Categoria2'
    CATEGORIA_3 = 'Categoria3'

    @staticmethod
    def list():
        return list(map(lambda c: c.value, Categoria))