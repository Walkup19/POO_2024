#   Formas de concatenar en Python

nombre = "Juan Perez"

especialidad = "Area Desarrollo de Software Multiplataforma"

carrera = "Ingenieria en Desarrollo y Gestion de Software"

#   Primer forma de concatenar

print("Mi nombre es" +nombre+ ", estoy en la especialidad de " +especialidad+ " y estudio " +carrera)
print("\n")

#   Segunda forma de concatenar

print("Mi nombre es ",nombre,", estoy en la especialidad de ",especialidad," y estudio ",carrera)
print("\n")

#   Tercera forma de concatenar

print(f"Mi nombre es {nombre}, estoy en la especialidad de {especialidad} y estudio {carrera}")
print("\n")

#   Cuarta forma de concatenar

print("Mi nombre es {}, estoy en la especialidad de {} y estudio {}".format(nombre, especialidad, carrera))
print("\n")

#   Quinta forma de concatenar

print('Mi nombre es ' +nombre+ ', estoy en la especialidad de ' +especialidad+ ' y estudio ' +carrera)
print('\n')