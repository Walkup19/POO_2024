

def agregar_pelicula(nombre_pelicula, lista_peliculas):
    lista_peliculas.append(nombre_pelicula)
    print("Película agregada con éxito!")

def remover_pelicula(nombre_pelicula, lista_peliculas):
    if nombre_pelicula in lista_peliculas:
        lista_peliculas.remove(nombre_pelicula)
        print("Película eliminada con éxito!")
    else:
        print("La película no está en la lista.")

def actualizar_pelicula(nombre_pelicula, nuevo_nombre, lista_peliculas):
    if nombre_pelicula in lista_peliculas:
        index = lista_peliculas.index(nombre_pelicula)
        lista_peliculas[index] = nuevo_nombre
        print("Película actualizada con éxito!")
    else:
        print("La película no está en la lista.")

def consultar_peliculas(lista_peliculas):
    if lista_peliculas:
        print("Lista de películas:")
        for pelicula in lista_peliculas:
            print("-", pelicula)
    else:
        print("La lista de películas está vacía.")

def buscar_pelicula(nombre_pelicula, lista_peliculas):
    if nombre_pelicula in lista_peliculas:
        print("La película está en la lista.")
    else:
        print("La película no está en la lista.")

def vaciar_lista(lista_peliculas):
    lista_peliculas.clear()
    print("Lista de películas vaciada con éxito!")
