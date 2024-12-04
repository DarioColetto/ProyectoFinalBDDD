from .reposotory import Repository
from .database import Conection
from models.cliente import Cliente

class ClienteRepo(Repository):

    def create(self, cliente: Cliente):
        query = """
            INSERT INTO clientes (nombre, email, telefono, direccion)
            VALUES (%s, %s, %s, %s);
        """
        params = (cliente.nombre, cliente.email, cliente.telefono, cliente.direccion)
        
        with Conection() as cnx:
            cnx.execute(query, params)
            cliente_id = cnx.lastrowid  # Devuelve el auto-incremented ID del nuevo objeto insertado.
        return cliente_id

    def get_all(self):

        clientes = []
        query = "SELECT * FROM clientes;"
        with Conection() as cnx:
            cnx.execute(query)
            rows = cnx.fetchall()

        for row in rows:    

            cliente = Cliente(row[0], row[1], row[2], row[3], row[4]) 
            clientes.append(cliente)
            
        return clientes

    def get(self, id:int):
        query = "SELECT * FROM clientes WHERE id_cliente=%s;"
        with Conection() as cnx:
            cnx.execute(query,  (id,))
            row = cnx.fetchone()

            if row:
                return Cliente(row[0], row[1], row[2], row[3], row[4])       
            return None


    def update(self, id: int, data: dict):
        # Construlle el SET de manera dinamica
        columns = ", ".join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE clientes SET {columns} WHERE id_cliente = %s;"
        params = list(data.values()) + [id]

        print(query)

        with Conection() as cnx:
            cnx.execute(query, params)            
        return f"cliente {id} actualizado."

    def delete(self, id: int):
            query = "DELETE FROM clientes WHERE id_cliente = %s;"
            with Conection() as cnx:
                cnx.execute(query, (id,))
            return f"cliente {id} eliminado."


    def getByNombre(self, nombre: str):
        clientes = []
        query = """ SELECT * FROM clientes WHERE nombre LIKE %s """
        with Conection() as cnx:
            # Usa un wildcard con parámetros seguros.
            cnx.execute(query, (f"%{nombre}%",))
            rows = cnx.fetchall()

            for row in rows:
                cliente = Cliente(row[0], row[1], row[2], row[3], row[4]) 
                clientes.append(cliente)

        return clientes


    