def main():
    # Solicitar dos números al usuario
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Realizar operaciones
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    # Manejar la división por cero
    if num2 != 0:
        division = num1 / num2
    else:
        division = "No se puede dividir por cero."

    # Mostrar resultados
    print("Suma:", num1, "+", num2, "=", suma)
    print("Resta:", num1, "-", num2, "=", resta)
    print("Multiplicación:", num1, "*", num2, "=", multiplicacion)
    print("División:", num1, "/", num2, "=", division)

if __name__ == "__main__":
    main()
