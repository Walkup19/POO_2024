def calcular_porcentaje(numero, porcentaje):
    """
    Calcula el porcentaje de un número dado.
    
    Args:
    - numero: El número del cual se calculará el porcentaje.
    - porcentaje: El porcentaje que se desea calcular.
    
    Returns:
    El resultado de calcular el porcentaje del número dado.
    """
    resultado = (porcentaje / 100) * numero
    return resultado

def main():
    # Solicitar al usuario el número y el porcentaje
    numero = float(input("Ingrese el número: "))
    porcentaje = float(input("Ingrese el porcentaje a calcular (sin el símbolo %): "))

    # Calcular el porcentaje del número dado
    resultado = calcular_porcentaje(numero, porcentaje)

    # Mostrar el resultado
    print(f"{porcentaje}% de {numero} es igual a {resultado}")

if __name__ == "__main__":
    main()