## Diseño de la Base de Datos

1. Entidades y Atributos:

- Productos (Entidad fuerte):
id_producto (PK), nombre, descripcion, categoria, precio, stock
- Clientes (Entidad fuerte):
id_cliente (PK), nombre, email, telefono, direccion
- Órdenes (Entidad débil, dependiente de Cliente y Producto):
id_orden (PK), id_cliente (FK), id_producto (FK), fecha, cantidad


2. Relaciones y Cardinalidades:

- Clientes tiene una relación de 1:N con Órdenes: Un cliente puede realizar varias órdenes.
- Productos tiene una relación de 1:N con Órdenes: Un producto puede ser parte de varias órdenes.
3. Cardinalidad:

- Clientes puede tener múltiples Órdenes (uno a muchos), pero una Orden pertenece a un solo Cliente.
- Productos puede tener múltiples Órdenes (uno a muchos), pero una Orden se refiere a un solo Producto.

### Restricciones de Integridad
1. Llaves Primarias y Foráneas:

- id_producto en Productos, id_cliente en Clientes, y id_orden en Órdenes son llaves primarias.
- id_cliente y id_producto en la tabla Órdenes son llaves foráneas referenciando a Clientes y Productos respectivamente.
2. Restricciones NOT NULL y UNIQUE:

- id_producto, nombre, precio, y stock en Productos deben ser NOT NULL.
- id_cliente, nombre, y email en Clientes deben ser NOT NULL, con email también UNIQUE.
- id_orden, id_cliente, id_producto, fecha, y cantidad en Órdenes deben ser NOT NULL.

### Operaciones en Cascada
- En Órdenes, para garantizar que la eliminación de un cliente o producto no borre en cascada sus órdenes, se usará ON DELETE RESTRICT.
- Para actualizaciones que cambien los IDs de clientes o productos, se puede usar ON UPDATE CASCADE para reflejar los cambios en Órdenes.

## Modelo del Sistema

1. Crear base de datos ej: ventas_en_linea

```sql
CREATE DATABASE databasename;
```
##### Cambiar 'databasename' por el nombre de su base de datos.

### Diagrama
![alt text](.\SQL\diagrama.png)

Las entidades clave son:

- Productos: Representan los artículos que están a la venta.
- Clientes: Representan los usuarios que realizan las compras.
- Órdenes: Cada registro representa una orden de compra de un cliente para un producto específico.


#### 2. Estructura de Tablas
```sql
CREATE TABLE Productos (
    id_producto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    categoria VARCHAR(50),
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);

CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(15),
    direccion TEXT
);

CREATE TABLE Ordenes (
    id_orden INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_producto INT NOT NULL,
    fecha DATE NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
)

```

#### 3. Datos Iniciales
Inserta algunos datos iniciales en las tablas para realizar pruebas:

```sql
-- Productos
INSERT INTO Productos (nombre, descripcion, categoria, precio, stock) VALUES
('Producto1', 'Descripción de Producto1', 'Categoría1', 10.00, 100),
('Producto2', 'Descripción de Producto2', 'Categoría1', 15.00, 50)

-- Clientes
INSERT INTO Clientes (nombre, email, telefono, direccion) VALUES
('Cliente1', 'cliente1@email.com', '1234567890', 'Dirección 1'),
('Cliente2', 'cliente2@email.com', '0987654321', 'Dirección 2')

-- Órdenes
INSERT INTO Ordenes (id_cliente, id_producto, fecha, cantidad) VALUES
(1, 1, '2024-01-01', 5),
(1, 2, '2024-01-02', 3)

```

# APP

- La app de gestion esta escrita en Python 3. 
- GUI esta realizada con los paquetes nativos Tk
- Es necesario instalar el conector mysql.

Para una guia mas detalla de myql:

https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html

## APP SETUP

### Instalacion del conector mysql

```
pip install mysql-connector-python
```

### Crear archivo `config.py`

Crear un archivo `config.py` en la carpeta raiz preferentemente, o ubicarlo en donde desee. El archivo contendra los datos de conexion a la base de datos en formato **dict**. 
Cambie los datos que crea necesarios como *password* y *databasename* (nombre de su base de datos).

```python
config = {
        'host':'127.0.0.1',
        'user':'root',
        'password':'password',
        'database':'dababasename'
}
```

### Importar `config`
En la carpeta */repository* se encuentra el archivo `database.py`.
Ahi se ecuentra los modulos **mysql** y **config**.

/repository/database.py
```python
import mysql.connector
from config import config
```

## EJECUCION

La entrada o punto de ejecucion es el archivo `__main__.py`