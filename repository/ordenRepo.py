from .reposotory import Repository
from .database import Conection
from models.orden import Orden

class OrdenRepo(Repository):

    def create(self, orden: Orden):
        query = """
            INSERT INTO ordenes (id_cliente, id_producto, fecha, cantidad)
            VALUES (%s, %s, %s, %s);
        """
        params = (orden.id_cliente, orden.id_producto, orden.fecha, orden.cantidad)
        
        with Conection() as cnx:
            cnx.execute(query, params)
            orden_id = cnx.lastrowid  # Devuelve el auto-incremented ID del nuevo objeto insertado.
        return orden_id

    def get_all(self):

        ordenes = []
        query = "SELECT * FROM ordenes;"
        with Conection() as cnx:
            cnx.execute(query)
            rows = cnx.fetchall()

        for row in rows:    

            orden = Orden(
                id_orden=row[0],
                id_cliente= row[1], 
                id_producto=row[2], 
                fecha=row[3],
                cantidad=  row[4]) 
            ordenes.append(orden)
            
        return ordenes

    def get(self, id:int):
        query = "SELECT * FROM ordenes WHERE id_orden=%s;"
        with Conection() as cnx:
            cnx.execute(query,  (id,))
            row = cnx.fetchone()

            if row:
                return Orden(
                id_orden=row[0],
                id_cliente= row[1], 
                id_producto=row[2], 
                fecha=row[3],
                cantidad=  row[4])        
            return None


    def update(self, id: int, data: dict):
        # Construlle el SET de manera dinamica
        columns = ", ".join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE orden SET {columns} WHERE id_orden = %s;"
        params = list(data.values()) + [id]

        with Conection() as cnx:
            cnx.execute(query, params)            
        return f"orden {id} actualizado."

    def delete(self, id: int):
            query = "DELETE FROM ordenes WHERE id_orden = %s;"
            with Conection() as cnx:
                cnx.execute(query, (id,))
            return f"orden {id} eliminado."




    