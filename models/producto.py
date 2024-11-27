from decimal import Decimal

from models.categoria import Categoria


class Producto:
    def __init__(self, id_producto: int, nombre: str, descripcion: str, categoria: Categoria, precio: float, stock: int):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    # Getters
    @property
    def id_producto(self):
        return self._id_producto

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def categoria(self):
        return self._categoria

    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self._stock

    # Setters
    @id_producto.setter
    def id_producto(self, value):
        if not isinstance(value, int | None):
            raise ValueError("El ID del producto debe ser un número entero.")
        self._id_producto = value

    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena de caracteres.")
        if not value or len(value) > 50:
            raise ValueError("El nombre del producto no debe estar vacío y debe tener un máximo de 50 caracteres.")
        self._nombre = value

    @descripcion.setter
    def descripcion(self, value):
        if not isinstance(value, str):
            raise ValueError("La descripción debe ser una cadena de caracteres.")
        self._descripcion = value.strip()

    @categoria.setter
    def categoria(self, value:Categoria):
        # if value not in list(Categoria):
        #     raise ValueError("La categoría debe ser una categoria valida")
        if not isinstance(value, Categoria):
            raise ValueError("La categoría debe ser categoria valida")
        self._categoria = value

    @precio.setter
    def precio(self, value):
        if not isinstance(value, (int, float, Decimal)):
            raise ValueError("El precio debe ser un número.")
        if value <= 0:
            raise ValueError("El precio debe ser mayor a 0.")
        self._precio = float(value)

    @stock.setter
    def stock(self, value):
        if not isinstance(value, int):
            raise ValueError("El stock debe ser un número entero.")
        if value < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = value

    def toDict(self)->dict:
        return{
            'id_producto':self.id_producto,
            'nombre':self.nombre,
            'descripcion':self.descripcion,
            'categoria':self.categoria.value,
            'precio':self.precio,
            'stock':self.stock

        }