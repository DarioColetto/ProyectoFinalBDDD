-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
-- ------------------------------------------------------
DROP DATABASE IF EXISTS ventas_en_linea;
CREATE DATABASE ventas_en_linea;
USE ventas_en_linea;
--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE `clientes` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `direccion` text,
  PRIMARY KEY (`id_cliente`),
  UNIQUE KEY `email` (`email`)
);


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



DROP TABLE IF EXISTS `productos`;
CREATE TABLE `productos` (
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text,
  `categoria` varchar(50) DEFAULT NULL,
  `precio` decimal(10,2) NOT NULL,
  `stock` int NOT NULL,
  PRIMARY KEY (`id_producto`),
  UNIQUE KEY `nombre` (`nombre`)
);


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


DROP TABLE IF EXISTS `ordenes`;
CREATE TABLE `ordenes` (
  `id_orden` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `id_producto` int NOT NULL,
  `fecha` date NOT NULL,
  `cantidad` int NOT NULL,
  PRIMARY KEY (`id_orden`),
  KEY `id_producto` (`id_producto`),
  KEY `idx_cliente` (`id_cliente`),
  CONSTRAINT `ordenes_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `ordenes_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Órdenes
INSERT INTO ordenes (id_cliente, id_producto, fecha, cantidad) VALUES
-- Órdenes para Cliente1
(1, 1, '2024-01-15', 5),
(1, 2, '2024-02-10', 3),
(1, 3, '2024-03-08', 2),
(1, 4, '2024-04-20', 1),
(1, 5, '2024-05-12', 4),
(1, 6, '2024-06-18', 2),
(1, 7, '2024-07-25', 6),
(1, 8, '2024-09-10', 3),
(1, 9, '2024-10-05', 7),
(1, 10, '2024-12-28', 5),

-- Órdenes para Cliente2
(2, 1, '2024-02-05', 1),
(2, 2, '2024-02-20', 2),
(2, 3, '2024-03-15', 3),
(2, 4, '2024-04-27', 4),
(2, 5, '2024-06-06', 5),
(2, 6, '2024-07-11', 1),
(2, 7, '2024-09-22', 2),
(2, 8, '2024-10-03', 3),
(2, 9, '2024-11-14', 4),
(2, 10, '2024-12-31', 5),

-- Órdenes para Cliente3
(3, 1, '2024-01-12', 2),
(3, 2, '2024-02-18', 4),
(3, 3, '2024-03-22', 6),
(3, 4, '2024-05-07', 3),
(3, 5, '2024-06-19', 1),
(3, 6, '2024-07-04', 2),
(3, 7, '2024-09-12', 5),
(3, 8, '2024-10-18', 4),
(3, 9, '2024-11-25', 2),
(3, 10, '2024-12-13', 1),

-- Órdenes para Cliente4
(4, 1, '2024-01-30', 12),
(4, 2, '2024-03-16', 4),
(4, 3, '2024-04-02', 8),
(4, 4, '2024-05-18', 4),
(4, 5, '2024-06-28', 11),
(4, 6, '2024-08-14', 5),
(4, 7, '2024-09-05', 2),
(4, 8, '2024-10-30', 14),
(4, 9, '2024-11-12', 2),
(4, 10, '2024-12-20', 11),

-- Órdenes para Cliente5
(5, 1, '2024-02-15', 3),
(5, 2, '2024-03-07', 5),
(5, 3, '2024-04-11', 6),
(5, 4, '2024-06-03', 5),
(5, 5, '2024-07-23', 12),
(5, 6, '2024-08-05', 7),
(5, 7, '2024-10-27', 16),
(5, 8, '2024-11-10', 15),
(5, 9, '2024-12-14', 21),
(5, 10, '2024-12-22', 7),

-- Órdenes para Cliente6
(6, 1, '2024-01-19', 3),
(6, 2, '2024-03-29', 6),
(6, 3, '2024-05-03', 7),
(6, 4, '2024-06-24', 16),
(6, 5, '2024-08-16', 11),
(6, 6, '2024-09-01', 12),
(6, 7, '2024-10-21', 6),
(6, 8, '2024-11-07', 16),
(6, 9, '2024-12-19', 2),
(6, 10, '2024-12-29', 14),

-- Órdenes para Cliente7
(7, 1, '2024-01-09', 1),
(7, 2, '2024-02-04', 7),
(7, 3, '2024-03-19', 8),
(7, 4, '2024-05-25', 5),
(7, 5, '2024-07-30', 12),
(7, 6, '2024-09-18', 22),
(7, 7, '2024-10-24', 17),
(7, 8, '2024-11-08', 7),
(7, 9, '2024-12-02', 1),
(7, 10, '2024-12-17', 6),

-- Órdenes para Cliente8
(8, 1, '2024-01-28', 10),
(8, 2, '2024-03-09', 8),
(8, 3, '2024-05-16', 6),
(8, 4, '2024-06-21', 8),
(8, 5, '2024-08-03', 1),
(8, 6, '2024-09-26', 2),
(8, 7, '2024-10-12', 18),
(8, 8, '2024-11-23', 8),
(8, 9, '2024-12-06', 9),
(8, 10, '2024-12-15', 2),

-- Órdenes para Cliente9
(9, 1, '2024-02-08', 2),
(9, 2, '2024-03-22', 20),
(9, 3, '2024-06-02', 7),
(9, 4, '2024-07-11', 1),
(9, 5, '2024-08-30', 1),
(9, 6, '2024-09-06', 5),
(9, 7, '2024-10-04', 9),
(9, 8, '2024-11-19', 3),
(9, 9, '2024-12-10', 2),
(9, 10, '2024-12-24', 12),

-- Órdenes para Cliente10
(10, 1, '2024-01-20', 2),
(10, 2, '2024-03-11', 10),
(10, 3, '2024-05-09', 3),
(10, 4, '2024-06-14', 7),
(10, 5, '2024-07-07', 1),
(10, 6, '2024-09-20', 2),
(10, 7, '2024-10-15', 14),
(10, 8, '2024-11-05', 10),
(10, 9, '2024-12-12', 2),
(10, 10, '2024-12-30', 1);



--Procedures

--Agregar nueva orden
DELIMITER $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `nueva_orden`(
    IN cliente INT, 
    IN producto INT, 
    IN cant INT, 
    IN fecha DATE,
    OUT id_orden INT
)
BEGIN
    DECLARE stock_disponible INT;
    DECLARE cliente_existente INT;

    START TRANSACTION;

    -- Check if the client exists
    SELECT COUNT(*) INTO cliente_existente
    FROM clientes
    WHERE id_cliente = cliente;

    IF cliente_existente = 0 THEN
        -- If client does not exist, rollback and set id_orden to NULL
        SET id_orden = NULL;
        ROLLBACK;
    ELSE
        -- Check stock availability
        SELECT stock INTO stock_disponible
        FROM productos
        WHERE id_producto = producto;

        IF stock_disponible >= cant THEN
            -- Insert the new order
            INSERT INTO ordenes (id_cliente, id_producto, fecha, cantidad)
            VALUES (cliente, producto, fecha, cant);

            -- Update product stock
            UPDATE productos
            SET stock = stock - cant
            WHERE id_producto = producto;

            -- Get the ID of the new order
            SET id_orden = LAST_INSERT_ID();

            COMMIT;
        ELSE
            -- Rollback if not enough stock
            SET id_orden = NULL; -- Indicate failure with NULL
            ROLLBACK;
        END IF;
    END IF;
END$$

DELIMITER ;
