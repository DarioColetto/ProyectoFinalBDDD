
from models.ordenDTO import OrdenDTO
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
        query = """SELECT Ordenes.Id_orden, Clientes.nombre AS cliente, Productos.nombre AS producto, Ordenes.cantidad, Ordenes.fecha
                FROM Ordenes
                INNER JOIN Clientes ON Ordenes.id_cliente = Clientes.id_cliente
                INNER JOIN Productos ON Ordenes.id_producto = Productos.id_producto;"""
        with Conection() as cnx:
            cnx.execute(query)
            rows = cnx.fetchall()

        for row in rows:    

            orden = OrdenDTO(
                id_orden=row[0],
                cliente= row[1], 
                producto=row[2],
                cantidad=  row[3],  
                fecha=row[4])
                
            ordenes.append(orden)
            
        return ordenes

    def get(self, id:int):
        query = """SELECT Ordenes.Id_orden, Clientes.nombre AS cliente, Productos.nombre AS producto, Ordenes.cantidad, Ordenes.fecha
                FROM Ordenes
                INNER JOIN Clientes ON Ordenes.id_cliente = Clientes.id_cliente
                INNER JOIN Productos ON Ordenes.id_producto = Productos.id_producto
                WHERE id_orden=%s;"""
        with Conection() as cnx:
            cnx.execute(query,  (id,))
            row = cnx.fetchone()

            if row:
                return OrdenDTO(
                id_orden=row[0],
                cliente= row[1], 
                producto=row[2],
                cantidad=  row[3],  
                fecha=row[4])        
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


    def getByName(self, nombre:str):
        ordenes = []
        query = """SELECT Ordenes.Id_orden, Clientes.nombre AS cliente, Productos.nombre AS producto, Ordenes.cantidad, Ordenes.fecha
                FROM Ordenes
                INNER JOIN Clientes ON Ordenes.id_cliente = Clientes.id_cliente
                INNER JOIN Productos ON Ordenes.id_producto = Productos.id_producto
                WHERE Clientes.nombre LIKE %s ;"""
        with Conection() as cnx:
            cnx.execute(query,  (f"{nombre}%",))
            rows = cnx.fetchall()

        for row in rows:    

            orden = OrdenDTO(
                id_orden=row[0],
                cliente= row[1], 
                producto=row[2],
                cantidad=  row[3],  
                fecha=row[4])
                
            ordenes.append(orden)
            
        return ordenes
                   
            

    def actualizar_cantidad_maxima(self, id_producto: int, cantidad_maxima: int):
        query = """
            UPDATE Ordenes
            SET cantidad = LEAST(cantidad, %s)
            WHERE id_producto = %s;
        """
        with Conection() as cnx:
            cnx.execute(query, (cantidad_maxima, id_producto))
            filas_afectadas = cnx.rowcount  # Cantidad de filas actualizadas
        return f"{filas_afectadas} Ã³rdenes actualizadas."