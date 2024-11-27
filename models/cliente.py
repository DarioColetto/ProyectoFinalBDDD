class Cliente:
    def __init__(self, id_cliente:int, nombre:str, email:str, telefono:str, direccion:str):
        self._id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

    # Getters
    @property
    def id_cliente(self):
        return self._id_cliente

    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email

    @property
    def telefono(self):
        return self._telefono

    @property
    def direccion(self):
        return self._direccion

    # Setters
    @nombre.setter
    def nombre(self, value:str):
        if not value or len(value) > 100:
            raise ValueError("El nombre del cliente no debe estar vacío y debe tener un máximo de 100 caracteres.")
        self._nombre = value

    @email.setter
    def email(self, value:str):
        if not value or "@" not in value or len(value) > 100:
            raise ValueError("El email no es válido o supera los 100 caracteres.")
        self._email = value

    @telefono.setter
    def telefono(self, value:str):
        if value and (not value.isdigit() or len(value) > 15):
            raise ValueError("El teléfono debe contener solo dígitos y no superar los 15 caracteres.")
        self._telefono = value or ""

    @direccion.setter
    def direccion(self, value:str):
        self._direccion = value or ""

    def toDict(self)->dict:
        return{
            'id_cliente':self.id_cliente,
            'nombre':self.nombre,
            'telefono':self.telefono,
            'direccion':self.direccion
        }
    