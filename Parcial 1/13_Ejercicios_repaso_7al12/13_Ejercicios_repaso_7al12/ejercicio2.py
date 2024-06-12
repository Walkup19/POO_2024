"""2.- 
Escribir un programa  que añada valores a una lista mientras que su longitud 
 sea menor a 120, y luego mostrar la lista: Usar un while y for"""

lista_while = []
contador = 0
try:
    while len(lista_while) < 120:
        lista_while.append(contador)
        contador += 1
except MemoryError:
    print("se ha llenado la memoria")

print("Lista creada con bucle while y manejo de excepción:", lista_while)

lista_for = []
try:
    for i in range(120):
        lista_for.append(i)
except MemoryError:
    print("se ha llenado la memoria")

print("Lista creada con bucle for y manejo de excepción:", lista_for)

