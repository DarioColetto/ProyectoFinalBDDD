from datetime import date

class OrdenDTO:
    def __init__(self, id_orden: int, id_cliente: int, cliente: str, id_producto: int, producto: str, fecha: date, cantidad: int):
        self._id_orden = id_orden
        self._id_cliente = id_cliente
        self.id_producto = id_producto
        self.cliente = cliente  # Usa el setter para validación
        self.producto = producto  # Usa el setter para validación
        self.fecha = fecha  # Usa el setter para validación
        self.cantidad = cantidad  # Usa el setter para validación

    # Getters
    @property
    def id_orden(self):
        return self._id_orden
    
    @property
    def id_cliente(self):
        return self._id_cliente

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
    def cliente(self, value: str):
        if not value or len(value) > 100:
            raise ValueError("El nombre del cliente no debe estar vacío y debe tener un máximo de 100 caracteres.")
        self._cliente = value

    @producto.setter
    def producto(self, value: str):
        if not value or len(value) > 100:
            raise ValueError("El nombre del producto no debe estar vacío y debe tener un máximo de 100 caracteres.")
        self._producto = value

    @fecha.setter
    def fecha(self, value: date):
        if not isinstance(value, date):
            raise ValueError("La fecha debe ser de tipo date.")
        self._fecha = value

    @cantidad.setter
    def cantidad(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("La cantidad debe ser un número entero positivo.")
        self._cantidad = value
