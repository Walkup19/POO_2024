"""4.- 
Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
  y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones"""

def tipo_de_dato(variable):
    if isinstance(variable, list):
        return "La variable es una lista."
    elif isinstance(variable, str):
        return "La variable es una cadena de texto."
    elif isinstance(variable, int):
        return "La variable es un entero."
    elif isinstance(variable, bool):
        return "La variable es un booleano."
    else:
        return "Tipo de dato desconocido."

def main():
   
    mi_lista = [1, 2, 3]
    mi_cadena = "Hola, mundo!"
    mi_entero = 42
    mi_logico = True

    print(tipo_de_dato(mi_lista))
    print(tipo_de_dato(mi_cadena))
    print(tipo_de_dato(mi_entero))
    print(tipo_de_dato(mi_logico))

if __name__ == "__main__":
    main()
