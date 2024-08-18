import mysql.connector
import os
import subprocess

def importar_bd():
    ruta_archivo_sql = os.path.join(os.path.dirname(__file__), "database", "constructora.sql")
    comando = f"mysql - u root -p constructora < {ruta_archivo_sql}"
    subprocess.run(comando, shell=True)

try:
    #importar bd antes de conectar
    importar_bd()
    
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "constructora",
    )

    cursor = conexion.cursor(buffered = True)

except Exception as excepcion:
    print(f"Error: {excepcion}")
    print(f"Tipo de error: {type(excepcion).__name__}")
    print("Ha ocurrido un problema, intenta despues.")