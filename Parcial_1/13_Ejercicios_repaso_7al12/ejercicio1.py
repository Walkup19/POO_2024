"""1.- 

 Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

 a.- Recorrer la lista y mostrarla
 b.- hacer una funcion que recorra la lista de numeros y devuelva un string
 c.- ordenarla y mostrarla
 d.- mostrar su longitud
 e.- buscar algun elemento que el usuario pida por teclado"""


def mostrar_lista(lista):
    print("La lista es:", ' '.join(map(str, lista)))

numeros = [4, 8, 2, 10, 5, 1, 7, 3]

mostrar_lista(numeros)

string_lista = ' '.join(map(str, numeros))
print("La lista como string es:", string_lista)

numeros.sort()
print("La lista ordenada es:", ' '.join(map(str, numeros)))

print("La longitud de la lista es:", len(numeros))

try:
    elemento_buscar = int(input("Ingrese un número para buscar en la lista: "))
    if elemento_buscar in numeros:
        print(f"El elemento {elemento_buscar} está en la lista.")
    else:
        print(f"El elemento {elemento_buscar} no está en la lista.")
except ValueError:
    print("Error: Ingrese un número válido.")

