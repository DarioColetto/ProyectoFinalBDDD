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
![alt text](https://github.com/DarioColetto/ProyectoFinalBDDD/blob/main/SQL/diagrama.png)

Las entidades clave son:

- Productos: Representan los artículos que están a la venta.
- Clientes: Representan los usuarios que realizan las compras.
- Órdenes: Cada registro representa una orden de compra de un cliente para un producto específico.


#### 2. Estructura de Tablas
```sql
CREATE TABLE productos (
    id_producto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    categoria VARCHAR(50),
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);

CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(15),
    direccion TEXT
);

CREATE TABLE ordenes (
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
Inserta algunos datos iniciales en las tablas para realizar pruebas  , ver archivos SQL !!.

Ejemplo:

```sql
-- Productos
INSERT INTO productos (nombre, descripcion, categoria, precio, stock) VALUES
('Producto1', 'Descripción de Producto1', 'Categoria1', 10.00, 100),
('Producto2', 'Descripción de Producto2', 'Categoria2', 15.00, 50),
('Producto3', 'Descripción de Producto3', 'Categoria3', 20.00, 30),
('Producto4', 'Descripción de Producto4', 'Categoria1', 25.00, 40),
('Producto5', 'Descripción de Producto5', 'Categoria2', 30.00, 20),
('Producto6', 'Descripción de Producto6', 'Categoria3', 35.00, 10),
('Producto7', 'Descripción de Producto7', 'Categoria1', 40.00, 15),
('Producto8', 'Descripción de Producto8', 'Categoria2', 45.00, 25),
('Producto9', 'Descripción de Producto9', 'Categoria3', 50.00, 35),
('Producto10', 'Descripción de Producto10', 'Categoria1', 55.00, 5);

-- Clientes
INSERT INTO clientes (nombre, email, telefono, direccion) VALUES
('Cliente1', 'cliente1@email.com', '1234567890', 'Dirección 1'),
('Cliente2', 'cliente2@email.com', '0987654321', 'Dirección 2'),
('Cliente3', 'cliente3@email.com', '5678901234', 'Dirección 3'),
('Cliente4', 'cliente4@email.com', '4321098765', 'Dirección 4'),
('Cliente5', 'cliente5@email.com', '6789012345', 'Dirección 5'),
('Cliente6', 'cliente6@email.com', '8901234567', 'Dirección 6'),
('Cliente7', 'cliente7@email.com', '2345678901', 'Dirección 7'),
('Cliente8', 'cliente8@email.com', '7654321098', 'Dirección 8'),
('Cliente9', 'cliente9@email.com', '3456789012', 'Dirección 9'),
('Cliente10', 'cliente10@email.com', '8765432109', 'Dirección 10');

-- Órdenes
INSERT INTO ordenes (id_cliente, id_producto, fecha, cantidad) VALUES
-- Órdenes para Cliente1
(1, 1, '2024-01-01', 5),
(1, 2, '2024-01-02', 3),
(1, 3, '2024-01-03', 2),
(1, 4, '2024-01-04', 1),
(1, 5, '2024-01-05', 4),
(1, 6, '2024-01-06', 2),
(1, 7, '2024-01-07', 6),
(1, 8, '2024-01-08', 3),
(1, 9, '2024-01-09', 7),
(1, 10, '2024-01-10', 5),

-- Órdenes para Cliente2
(2, 1, '2024-02-01', 1),
(2, 2, '2024-02-02', 2),
(2, 3, '2024-02-03', 3),
(2, 4, '2024-02-04', 4),
(2, 5, '2024-02-05', 5),
(2, 6, '2024-02-06', 1),
(2, 7, '2024-02-07', 2),
(2, 8, '2024-02-08', 3),
(2, 9, '2024-02-09', 4),
(2, 10, '2024-02-10', 5),

-- Órdenes para Cliente3
(3, 1, '2024-03-01', 2),
(3, 2, '2024-03-02', 4),
(3, 3, '2024-03-03', 6),
(3, 4, '2024-03-04', 3),
(3, 5, '2024-03-05', 1),
(3, 6, '2024-03-06', 2),
(3, 7, '2024-03-07', 5),
(3, 8, '2024-03-08', 4),
(3, 9, '2024-03-09', 2),
(3, 10, '2024-03-10', 1);

-- Repite este patrón para Clientes4 a Clientes10 asegurándote de variar fechas, productos y cantidades.

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

### Crear o modificar archivo `config.py`

Crear o modificar el archivo `config.py` en la carpeta raiz preferentemente, o ubicarlo en donde desee. El archivo contendra los datos de conexion a la base de datos en formato **dict**. 
Cambie los datos que crea necesarios como *password* y *databasename* (nombre de su base de datos).

```python
config = {
        'host':'127.0.0.1',
        'user':'root',
        'password':'password',
        'database':'databasename'
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


### EJEMPLOS DE VISTA 
![alt text](https://github.com/DarioColetto/ProyectoFinalBDDD/blob/main/img/clientes.PNG)
![alt text](https://github.com/DarioColetto/ProyectoFinalBDDD/blob/main/img/addclientes.PNG)
![alt text](https://github.com/DarioColetto/ProyectoFinalBDDD/blob/main/img/buscarcliente.PNG)
![alt text](https://github.com/DarioColetto/ProyectoFinalBDDD/blob/main/img/delcliente.PNG)
