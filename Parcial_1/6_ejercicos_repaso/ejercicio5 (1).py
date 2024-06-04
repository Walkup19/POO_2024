def main():
    # Solicitar dos números al usuario
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    # Determinar el número más pequeño y más grande
    start_num = min(num1, num2)
    end_num = max(num1, num2)

    # Mostrar todos los números entre num1 y num2
    print("Los números entre", num1, "y", num2, "son:")
    for num in range(start_num + 1, end_num):
        print(num, end=" ")

if __name__ == "__main__":
    main()