def agregar_pelicula(pelicula, lista_peliculas):
    lista_peliculas.append(pelicula)
    print("Película agregada exitosamente.")
    
def remover_pelicula(pelicula, lista_peliculas):
    if pelicula in lista_peliculas:
        lista_peliculas.remove(pelicula)
        print("Película eliminada exitosamente.")
    else:
        print("La película no está en la lista.")
        
def consultar_peliculas(lista_peliculas):
    if lista_peliculas:
        print("Lista de películas:")
        for pelicula in lista_peliculas:
            print("-", pelicula)
            
    else:
        print("La lista de películas está vacía.")