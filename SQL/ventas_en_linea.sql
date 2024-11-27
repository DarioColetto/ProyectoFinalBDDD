-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
-- ------------------------------------------------------

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
INSERT INTO `clientes` VALUES 
(1,'Cliente1','cliente1@email.com','123456789','Dirección 1'),
(2,'CLiente2','cliente2@email.com','987654321','Direccion45 '),
(3,'Clientea3','email@blabla','1234569','siempre Viva 1235'),
(4,'Cliente4','pepe@pepe','21311','pepito 123');
UNLOCK TABLES;

--
-- Table structure for table `ordenes`
--

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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `ordenes`
--

LOCK TABLES `ordenes` WRITE;
INSERT INTO `ordenes` VALUES (1,1,1,'2024-01-01',5),(2,1,2,'2024-01-02',3),(3,1,3,'2024-11-25',67);
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
INSERT INTO `productos` VALUES 
(1,'Producto1','Descripción de Producto1','Categoria1',10.00,100),
(2,'Prodcuto62','Descripcion del producto 62','Categoria1',15.00,50),
(3,'P1','Latest model with advanced features','Categoria3',699.99,50);
UNLOCK TABLES;

