from datetime import date


class Orden:
    def __init__(self, id_orden:int, id_cliente:int, id_producto:int, fecha:date, cantidad:int):
        self._id_orden = id_orden
        self.id_cliente = id_cliente
        self.id_producto = id_producto
        self.fecha = fecha
        self.cantidad = cantidad

    # Getters
    @property
    def id_orden(self):
        return self._id_orden

    @property
    def id_cliente(self):
        return self._id_cliente

    @property
    def id_producto(self):
        return self._id_producto

    @property
    def fecha(self):
        return self._fecha

    @property
    def cantidad(self):
        return self._cantidad

    # Setters
    @id_cliente.setter
    def id_cliente(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El ID de cliente debe ser un número entero positivo.")
        self._id_cliente = value

    @id_producto.setter
    def id_producto(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El ID de producto debe ser un número entero positivo.")
        self._id_producto = value

    @fecha.setter
    def fecha(self, value):
        if not isinstance(value, date):
            raise ValueError("La fecha debe ser de tipo date.")
        self._fecha = value

    @cantidad.setter
    def cantidad(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("La cantidad debe ser un número entero positivo.")
        self._cantidad = value