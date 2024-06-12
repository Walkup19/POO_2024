from gestor_peliculas import *

lista_peliculas = []

while True:
    print("\n*** Menú ***")
    print("1. Agregar película")
    print("2. Eliminar película")
    print("3. Actualizar película")
    print("4. Consultar películas")
    print("5. Buscar película")
    print("6. Vaciar lista de películas")
    print("7. Salir")

    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        nombre_pelicula = input("Ingrese el nombre de la película: ")
        agregar_pelicula(nombre_pelicula, lista_peliculas)
        
    elif opcion == "2":
        nombre_pelicula = input("Ingrese el nombre de la película a eliminar: ")
        remover_pelicula(nombre_pelicula, lista_peliculas)
        
    elif opcion == "3":
        nombre_pelicula = input("Ingrese el nombre de la película a actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre de la película: ")
        actualizar_pelicula(nombre_pelicula, nuevo_nombre, lista_peliculas)
        
    elif opcion == "4":
        consultar_peliculas(lista_peliculas)
       
    elif opcion == "5":
        nombre_pelicula = input("Ingrese el nombre de la película a buscar: ")
        buscar_pelicula(nombre_pelicula, lista_peliculas)
        
    elif opcion == "6":
        vaciar_lista(lista_peliculas)
        
    elif opcion == "7":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número de opción válido.")
