def main():
    # Iterar sobre las tablas del 1 al 10
    for tabla in range(1, 11):
        print("Tabla del", tabla)
        print("--------------")

        # Generar las multiplicaciones del 1 al 10 para esta tabla
        for multiplicador in range(1, 11):
            resultado = tabla * multiplicador
            print(tabla, "x", multiplicador, "=", resultado)
        
        # Agregar un espacio en blanco entre cada tabla para mejor legibilidad
        print()

if __name__ == "__main__":
    main()