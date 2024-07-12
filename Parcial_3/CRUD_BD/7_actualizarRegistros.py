from conexionBD import *
try:
   micursor=conexion.cursor()

   sql="update clientes set tel='6181112233' where id='3'"
   micursor.execute(sql)
   conexion.commit()
except:
   print("Ocurrio un problema con el servidor... por favor intentalo más tarde...")
else:      
   print(f"Registro Actualizado Correctamente")
