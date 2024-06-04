"""

List (Array)
Son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un índice numérico

Nota: sus valores sí son modificados

La lista es una colección ordenada y modificable.
Permite miembros duplicados.

"""

#Ejemplo 1: crear una lista de números e imprimir su contenido

numeros = [1, 2, 3, 4, 5]

#Recorrer la lista con un ciclo for
# for i in numeros:
#     print(i)

#Recorrer la lista con un ciclo while
# i = 0
# while i <= len(numeros) - 1:
#     print(numeros[i])
#     i += 1


#Ejemplo 2: crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

continentes = ["America", "Europa", "Africa", "Asia", "Oceania", "Antartida"]

buscarPalabra = input("Ingresa la palabra a buscar: ")

for iterador in continentes:
    if buscarPalabra == continentes[iterador]:
        print(f"'{buscarPalabra}' encontrado en la posicion {iterador}")
    else:
        print("Palabra no encontrada.")
