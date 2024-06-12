"""2.- 
Escribir un programa  que añada valores a una lista mientras que su longitud 
 sea menor a 120, y luego mostrar la lista: Usar un while y for"""

lista_while = []
try:
    while len(lista_while) < 120:
        numero = int(input("Ingrese un número para la lista (o '0' para finalizar): "))
        if numero == 0:
            break
        lista_while.append(numero)
except MemoryError:
    print("¡Se ha llenado la memoria!")

print("Lista creada con bucle while y manejo de excepción:", lista_while)

lista_for = []
try:
    for _ in range(120):
        numero = int(input("Ingrese un número para la lista (o '0' para finalizar): "))
        if numero == 0:
            break
        lista_for.append(numero)
except MemoryError:
    print("¡Se ha llenado la memoria!")

print("Lista creada con bucle for y manejo de excepción:", lista_for)


