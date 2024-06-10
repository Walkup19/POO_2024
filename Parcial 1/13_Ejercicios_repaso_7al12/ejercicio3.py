"""3.- 
Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
 palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
 el contenido de la lista en mayusculas"""

def lista_vacia(lista):
    return len(lista) == 0

def llenar_lista(lista):
    while True:
        try:
            entrada = input("Ingresa una palabra o frase (o 'fin' para terminar): ")
            if entrada.lower() == 'fin':
                break
            lista.append(entrada)
        except KeyboardInterrupt:
            print("\nOperación interrumpida por el usuario.")
            break

def imprimir_en_mayusculas(lista):
    for elemento in lista:
        print(elemento.upper())

mi_lista = []

if lista_vacia(mi_lista):
    print("La lista está vacía.")
    print("Comienza a llenar la lista:")
    llenar_lista(mi_lista)
else:
    print("La lista ya tiene elementos.")

print("Contenido de la lista en mayúsculas:")
imprimir_en_mayusculas(mi_lista)


