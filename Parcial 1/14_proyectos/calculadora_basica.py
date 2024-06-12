def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b
def potencia(a, b):
    return a ** b
def raiz(a):
    if a < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    return math.sqrt(a)
while True:
    print("\n*** Calculadora ***")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Salir")

    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("Resultado:", suma(num1, num2))
    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("Resultado:", resta(num1, num2))
    elif opcion == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("Resultado:", division(num1, num2))
    elif opcion == "5":
        num1 = float(input("Ingrese la base: "))
        num2 = float(input("Ingrese el exponente: "))
        print("Resultado:", potencia(num1, num2))
    elif opcion == "6":
        num = float(input("Ingrese el número: "))
        print("Resultado:", raiz(num))
    elif opcion == "7":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número de opción válido.")
