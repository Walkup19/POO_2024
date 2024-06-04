"""una funcion es un conjunto de instruccines agrupadas bajo un nombre en particular
como un programa mas pequeño que cumple con una funcion espesifica la funcion se puede 
reutilizar con el simple hecho de invocarla es decirl mandarla llamar


#syntax:
def nombreMiFuncion (parametros):
    bloqueo o conjunto de instrucciones

nombreMiFuncion(parametros)

la funcion puede ser de 4 tipos
1- funcion que no recibe parametros y no regresan valor
2- funcion que no recibe parametros y regresan valor
3- funcion que recibe parametros y no regresan valor
4- funcion que recibe parametros y regresan valor"""

#1- funcion que no recibe parametros y no regresan valor
def solicitarpaciente():
    nombre=input("insertar nombre completo: ")

solicitarpaciente()

#2- funcion que no recibe parametros y regresan valor
def suma():
    n1=int(input("numero #1: "))
    n2=int(input("numero #2: "))
    suma=n1+n2
    print(f"{n1} + {n2} = {suma}")
    return suma
suma()

resultado_suma = suma()
print(f"la suma es: {suma}")

#3- funcion que recibe parametros y no regresan valor

def suma(n1,n2):
    suma=n1+n2
    print(f"{n1} + {n2} = {suma}")

n1=int(input("numero #1: "))
n2=int(input("numero #2: "))
suma(n1,n2)

resultado_suma = suma()
print(f"la suma es: {resultado_suma}")

#Ejemplo 4 sumar dos numeros
#4- funcion que recibe parametros y regresan valor
def suma(num1,num2):
   
    suma=num1+num2
    print(f"la suma es:{suma}")

n1=int(input("Numero #1;"))
n2=int(input("Numero #2;"))
suma(n1,n2)


"""crear un programa que solicite a traves de una funcion la siguiente informacion:
nombre, edad, estatura, tipo de sangre.
usa los 4 tipos de funciones"""
def myfunc():
    name = input("nombre del paciente: ")
    age = int(input("edad del paciente: "))
    altura = int(input("altura del paciente en metros: "))
    bloot_type = input("tipo de sangre: ")

def myfunc():
    name = input("nombre del paciente: ")
    age = int(input("edad del paciente: "))
    altura = int(input("altura del paciente en metros: "))
    bloot_type = input("tipo de sangre: ")
