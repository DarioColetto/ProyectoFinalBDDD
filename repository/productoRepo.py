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
            with Conection() as cnx:
                cnx.execute(query, (id,))
            return f"Producto {id} eliminado."


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
        

    def getByCategoria(self, categoria:Categoria):
        pass
    