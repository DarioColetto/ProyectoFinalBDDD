import mysql.connector
from config import config

class Conection:

    def __init__(self):
        self.db = mysql.connector.connect(**config)
                                                                    
                    

    def __enter__(self):
        if self.db.is_connected():
            print("Conexión exitosa a la base de datos.")
        return self.db.cursor()  # Retorna el cursor para uso dentro del contexto

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.commit()
        cursor = self.db.cursor()
        cursor.close()  # Cierra el cursor
        self.db.close()  # Cierra la conexión
        print("Conexión cerrada:", not self.db.is_connected())  # Confirma cierre de conexión
        return False  # Permite que las excepciones se propaguen si ocurren

# Prueba de conexión
if __name__ == '__main__':
    cnx = Conection()
    with cnx as cursor:
        cursor.execute("SELECT DATABASE();")  # Ejemplo: consulta la base de datos actual
        result = cursor.fetchone()
        print("Base de datos seleccionada:", result[0]) if result else print("No hay base de datos seleccionada.")
    