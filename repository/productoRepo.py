from models.categoria import Categoria
from .reposotory import Repository
from .database import Conection
from models.producto import Producto

class ProductoRepo(Repository):

    def create(self, producto: Producto):
        query = """
            INSERT INTO productos (nombre, descripcion, precio, stock, categoria)
            VALUES (%s, %s, %s, %s, %s);
        """
        params = (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.categoria.value)
        
        with Conection() as cnx:
            cnx.execute(query, params)
            producto_id = cnx.lastrowid  # Devuelve el auto-incremented ID del nuevo objeto insertado.
        return producto_id

    def get_all(self):

        productos = []
        query = "SELECT * FROM productos;"
        with Conection() as cnx:
            cnx.execute(query)
            rows = cnx.fetchall()

        for row in rows:    

            producto = Producto(
                id_producto= row[0], 
                nombre= row[1], 
                descripcion= row[2],
                categoria= Categoria(row[3]),
                precio= row[4], 
                stock= row[5]) 
            
            productos.append(producto)
            
        return productos

    def get(self, id:int):
        query = "SELECT * FROM productos WHERE id_producto=%s;"
        with Conection() as cnx:
            cnx.execute(query,  (id,))
            row = cnx.fetchone()

            if row:
                return Producto(
                id_producto= row[0], 
                nombre= row[1], 
                descripcion= row[2],
                categoria= Categoria(row[3]),
                precio= row[4], 
                stock= row[5]) 
                   
            return None


    def update(self, id: int, data: dict):
        # Construlle el SET de manera dinamica
        columns = ", ".join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE productos SET {columns} WHERE id_producto = %s;"
        params = list(data.values()) + [id]

        with Conection() as cnx:
            cnx.execute(query, params)            
        return f"Producto {id} actualizado."

    def delete(self, id: int):
            query = "DELETE FROM productos WHERE id_producto = %s;"
            
            try:
                with Conection() as cnx:
                    cnx.execute(query, (id,))
                return True
            except:
                return False


    def getByNombre(self, nombre: str):
        productos = []
        query = """ SELECT * FROM productos WHERE nombre LIKE %s """
        with Conection() as cnx:
            # Usa un wildcard con parámetros seguros.
            cnx.execute(query, (f"%{nombre}%",))
            rows = cnx.fetchall()

            for row in rows:
                producto = Producto(
                    id_producto=row[0],
                    nombre=row[1],
                    descripcion=row[2],
                    categoria=Categoria(row[3]),
                    precio=row[4],
                    stock=row[5]
                )
                productos.append(producto)

        return productos
        

    def getByCategoria(self, categoria:str):
        productos = []
        query = """ SElECT * FROM productos WHERE categoria = %s """
        with Conection() as cnx:
            # Usa un wildcard con parámetros seguros.
            cnx.execute(query, (categoria,))
            rows = cnx.fetchall()

            for row in rows:
                producto = Producto(
                    id_producto=row[0],
                    nombre=row[1],
                    descripcion=row[2],
                    categoria=Categoria(row[3]),
                    precio=row[4],
                    stock=row[5]
                )
                productos.append(producto)

        return productos


    def getOneByName(self, nombre:str):
        query = "SELECT * FROM productos WHERE nombre=%s;"
        with Conection() as cnx:
            cnx.execute(query,  (nombre,))
            row = cnx.fetchone()

            if row:
                return Producto(
                id_producto= row[0], 
                nombre= row[1], 
                descripcion= row[2],
                categoria= Categoria(row[3]),
                precio= row[4], 
                stock= row[5]) 
                   
            return None

    def productosMasVendidos(self):

        
        query ="""SELECT Productos.nombre, SUM(ordenes.cantidad) AS total_vendido
                    FROM ordenes
                    JOIN Productos ON ordenes.id_producto = Productos.id_producto
                    GROUP BY Productos.nombre
                    HAVING total_vendido > 0
                    ORDER BY total_vendido DESC;"""

    
        with Conection() as cnx:
            cnx.execute(query)
            rows = cnx.fetchall()

        return rows
    
    def getStockByName(self, nombre:str ):
        query = "SELECT stock FROM productos WHERE nombre=%s;"
        with Conection() as cnx:
            cnx.execute(query,  (nombre,))
            row = cnx.fetchone()

            if row:
                return row