from datetime import date


class OrdenDTO:
    def __init__(self, id_orden:int, cliente:str, producto:str, fecha:date, cantidad:int):
        self._id_orden = id_orden
        self.cliente = cliente
        self.producto = producto
        self.fecha = fecha
        self.cantidad = cantidad

    # Getters
    @property
    def id_orden(self):
        return self._id_orden

    @property
    def cliente(self):
        return self._cliente

    @property
    def producto(self):
        return self._producto

    @property
    def fecha(self):
        return self._fecha

    @property
    def cantidad(self):
        return self._cantidad

    # Setters
    @cliente.setter
    def cliente(self,  value:str):
        if not value or len(value) > 100:
            raise ValueError("El nombre del cliente no debe estar vacío y debe tener un máximo de 100 caracteres.")
        self._cliente = value

    @producto.setter
    def producto(self,  value:str):
        if not value or len(value) > 100:
            raise ValueError("El nombre del cliente no debe estar vacío y debe tener un máximo de 100 caracteres.")

        self._producto = value

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