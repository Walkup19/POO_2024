import mysql.connector
try:
#Conectar con la BD MySQL
  conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
)
except Exception as e:
    #print(f"Error:{e}")
    #print(f"Tipo de error:{type(e).__name__}")
    print("Ocurrio un problema con el servidor... por favor intentalo más tarde...")

   