"""
List (Array)
son colecciones o conjuntos de datos/valor bajo un mismo nombre, para acceder a los valores
se hace con un indice numerico


Nota: sus valores si son modificables

la lista es una coleccion ordenada y modificable permite miembros duplicados
"""
"""

#ejemplo 1- crear una lista de numeros e imprimir el contenido
numeros = [23,34]
print(numeros[0])

#recorrer una lista con un for
numeros = [23,34]
for i in numeros:
    print(i)

#recorrer una lista con while
numeros = [23,34]
i=0
while i<= len(numeros) -1:
    print(numeros[i])
    i+=1

#ejemplo 2
#crear una lista de palabras, posteriormente buscar la coincidencia de una palabra

palabra = ["hola","utd", "como", "estas", "ok", "ok", "naranja"]
palabra_buscar = input("inserta palabra a buscar: ")

if palabra_buscar in palabra:
    for i, p in enumerate(palabra):
        if p == palabra_buscar:
            print(f"Encontré la palabra en la posición {i}")
else:
    print("No encontré la palabra en la lista")"""

"""palabra = ["hola", "utd", "como", "estas", "ok", "ok", "naranja"]
palabra_buscar = input("inserta palabra a buscar: ")

encontrada = False
i = 0
while i < len(palabra):
    if palabra[i] == palabra_buscar:
        print(f"Encontré la palabra en la posición {i}")
        encontrada = True
    i += 1

if not encontrada:
    print("No encontré la palabra en la lista")  """ 

"""
numeros=[23,34,23]
print(numeros)

numeros.append(100)
print(numeros)
numeros.insert(3,200)
print(numeros)

numeros.remove(100)
print(numeros)
numeros.pop(0)
print(numeros)"""

#Ejemplo 4 crear un lista multilinea (matriz) para agregar los nombres y numeros telefonicos
"""
agenda=[
    ["Carlos",6181234567],
    ["Leo",66734824]
    ["Sebastian",65386956],
    ["Pedro", 61828383]
]

print(agenda)
for i in agenda:
    print(f"{agenda.index(i)+1.-{i}")"""

#ejemplo 5 crear un programa que permita gestionar (administrar) peliculas, colocar un menu de opciones para agregar, remover, consultar pleiculas.
#Notas:
#1-Utilizar funciones y mandar llamar desde otro archivo
#2-Utilizar listas para almacenar los nombres de peliculas

from gestor_peliculas import *

lista_peliculas = []

while True:
    print("\n*** Menú ***")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Salir")

    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        nombre_pelicula = input("Ingrese el nombre de la película: ")
        agregar_pelicula(nombre_pelicula, lista_peliculas)
        
    elif opcion == "2":
        nombre_pelicula = input("Ingrese el nombre de la película a eliminar: ")
        remover_pelicula(nombre_pelicula, lista_peliculas)
        
        
    elif opcion == "3":
        consultar_peliculas(lista_peliculas)
       
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número de opción válido.")
   