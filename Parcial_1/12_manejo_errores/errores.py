"""los errores de ejecucion en un lenguaje de programacion se presenta cuando existe una anomalia dentro de la ejecucion del codigo
,lo cual provoca que se detenga la ejecucion del SW con el control y manejo de exepsiones sera posible minimizar o evitar la 
interrupcion del programa debido a una excepcion"""

#Ejemplo 1 cuando una variable no se genera

"""try:
   nombre=input("Introduce el nombre completo de una persona:")

   if len(nombre)>0:
     nombre_usuario="El nombre completo del usuario es:"+nombre

   print(nombre_usuario)
except:
   print("Es necesario introducir un nombre de usuario... verifica por favor")

x=3+4
print("el valor de x es:"+str(x))"""

#Ejemplo 2 cuando se solicita un numero y se ingresa otra cosa

"""try:
 numero=int(input("Ingrese un numero entero:"))
 if numero > 0:
  print("Soy un numero entero positivo")
 elif numero==0:
  print("Soy un numero entero neutro")
 else:
  print("Soy un numero entero negativo")  
except ValueError:
 print("Introduce un valor numerico entero")"""

 #Ejemplo 3 Generan multiples excepciones
try:
 numero=int(input("Introduce un numero:"))

 print("El cuadrado del numero es: "+str(numero*numero))
except ValueError:
 print("Introduce un valor numerico entero")  
except TypeError:
 print("Se debe convertir el numero a entero")  
else:
 print("No se presentaron errores de ejecucion") 
finally:
 print("Termine la ejecucion") 
     