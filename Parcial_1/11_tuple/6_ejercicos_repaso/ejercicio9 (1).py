def main():
    # Variable para almacenar el número ingresado por el usuario
    numero = 0
    
    # Bucle para solicitar números al usuario
    while numero != 111:
        numero = int(input("Ingrese un número (o 111 para salir): "))
        
        # Verificar si se debe salir del bucle
        if numero == 111:
            print("Saliendo del programa...")
            break
        else:
            print("Número ingresado:", numero)

if __name__ == "__main__":
    main()