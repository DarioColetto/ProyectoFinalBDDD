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
