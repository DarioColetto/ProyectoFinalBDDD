
from datetime import date, datetime
from models.ordenDTO import OrdenDTO
from .reposotory import Repository
from .database import Conection
from models.orden import Orden

class OrdenRepo(Repository):

    def create(self, orden: Orden):
        query = "CALL nueva_orden(%s, %s, %s, %s, @id_orden);"
        get_id_query = "SELECT @id_orden;"
        params = (orden.id_cliente, orden.id_producto, orden.cantidad, orden.fecha)

        with Conection() as cnx:
            # Execute the stored procedure
            cnx.execute(query, params)
            # Fetch the output parameter
            cnx.execute(get_id_query)
            result = cnx.fetchone()
            orden_id = result[0] if result else None  # Get the returned ID or None

        return orden_id

    def get_all(self):

        ordenes = []
        query = """SELECT ordenes.id_orden, clientes.id_cliente as id_cliente, clientes.nombre AS cliente, productos.id_producto,  productos.nombre AS producto, ordenes.cantidad, ordenes.fecha
                FROM ordenes
                INNER JOIN clientes ON ordenes.id_cliente = clientes.id_cliente
                INNER JOIN productos ON ordenes.id_producto = productos.id_producto
                ORDER BY ordenes.id_orden;"""
        with Conection() as cnx:
            cnx.execute(query)
            rows = cnx.fetchall()

        for row in rows:    

            orden = OrdenDTO(
                id_orden=row[0],
                id_cliente = row[1],
                cliente= row[2], 
                id_producto = row[3],
                producto=row[4],
                cantidad= row[5],
                fecha=  row[6])
                
                
            ordenes.append(orden)
            
        return ordenes

    def get(self, id:int):
        query = """SELECT ordenes.id_orden, clientes.id_cliente as id_cliente, clientes.nombre AS cliente, productos.id_producto,  productos.nombre AS producto, ordenes.cantidad, ordenes.fecha
                FROM ordenes
                INNER JOIN clientes ON ordenes.id_cliente = clientes.id_cliente
                INNER JOIN productos ON ordenes.id_producto = productos.id_producto
                WHERE id_orden=%s;"""
        with Conection() as cnx:
            cnx.execute(query,  (id,))
            row = cnx.fetchone()

            if row:
                return  OrdenDTO(
                id_orden=row[0],
                id_cliente = row[1],
                cliente= row[2], 
                id_producto = row[3],
                producto=row[4],
                cantidad= row[5],
                fecha=  row[6])
            return None

    def getOrden(self, id:int):
        query = """SELECT ordenes.Id_orden, Clientes.id_cliente, Productos.id_producto, ordenes.cantidad, ordenes.fecha
                FROM ordenes
                INNER JOIN Clientes ON ordenes.id_cliente = Clientes.id_cliente
                INNER JOIN Productos ON ordenes.id_producto = Productos.id_producto
                WHERE id_orden=%s;"""
        with Conection() as cnx:
            cnx.execute(query,  (id,))
            row = cnx.fetchone()

            if row:
                return Orden(
                id_orden=row[0],
                id_cliente= row[1], 
                id_producto=row[2],
                cantidad=  row[3],  
                fecha=row[4])        
            return None

    def update(self, id: int, data: dict):
        # Construlle el SET de manera dinamica
        columns = ", ".join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE ordenes SET {columns} WHERE id_orden = %s;"
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
        query = """SELECT ordenes.id_orden, clientes.id_cliente as id_cliente, clientes.nombre AS cliente, productos.id_producto,  productos.nombre AS producto, ordenes.cantidad, ordenes.fecha
                FROM ordenes
                INNER JOIN clientes ON ordenes.id_cliente = clientes.id_cliente
                INNER JOIN productos ON ordenes.id_producto = productos.id_producto
                WHERE clientes.nombre LIKE %s 
                ORDER BY clientes.nombre ;"""
        with Conection() as cnx:
            cnx.execute(query,  (f"{nombre}%",))
            rows = cnx.fetchall()

        for row in rows:    

            orden = OrdenDTO(
                id_orden=row[0],
                id_cliente = row[1],
                cliente= row[2], 
                id_producto = row[3],
                producto=row[4],
                cantidad= row[5],
                fecha=  row[6])
                
            ordenes.append(orden)
            
        return ordenes
                   
            

    def actualizar_cantidad_maxima(self, id_producto: int, cantidad_maxima: int):
        query = """
            UPDATE ordenes
            SET cantidad = LEAST(cantidad, %s)
            WHERE id_producto = %s;
        """
        with Conection() as cnx:
            cnx.execute(query, (cantidad_maxima, id_producto))
            filas_afectadas = cnx.rowcount  # Cantidad de filas actualizadas
        return f"{filas_afectadas} Ã³rdenes actualizadas."