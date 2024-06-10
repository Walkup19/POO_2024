def main():
    # Inicializar contadores
    aprobados = 0
    reprobados = 0

    # Solicitar calificaciones de los 15 alumnos
    for i in range(1, 16):
        calificacion = float(input(f"Ingrese la calificación del alumno {i}: "))
        
        # Verificar si el alumno aprobó o no
        if calificacion >= 8.0:
            aprobados += 1
        else:
            reprobados += 1

    # Mostrar resultados
    print("Número de alumnos que aprobaron:", aprobados)
    print("Número de alumnos que no aprobaron:", reprobados)

if __name__ == "__main__":
    main()
