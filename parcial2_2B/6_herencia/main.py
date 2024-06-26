from coches import *


#Crear un objetos o instanciar la clase
print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)

#Mostrar los valores inicales del objeto o instancia de la clase
coche1.getInfo()



# Crear otro objeto e imprimir los valores
# print("Objeto 2")
# coche2=Coches("Azul","Nissan","2020",180,150,6)
# coche2.setColor("Blue Demon")
# #Imprimir los valores del otro objeto
# coche2.getInfo()

#Implementar la visibilidad

# print(coche1.atributo_publico)
# print(coche1.__atributo_privado) #Incorrecto
# print(coche1.getAtributoPrivado())
# #coche1.__MetodoPrivado() #Incorrecto
# coche1.MetodoPublico()


#Crear un objeto o instanciar una clase
print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)
coche1.getInfo()

#Crear un objeto o instanciar una clase
print("Objeto 2")
coche2=Coches("Azul","Nissan","2020",180,150,6)
coche2.getInfo()

#Crear los objetos o instancias de las clases camiones y camionetas
print("Objeto 3")
camion1=Camiones("Negro","Dina","2020",180,300,12,8,2500)
camion1.getInfo()

#Crear los objetos o instancias de las clases camiones y camionetas
print("Objeto 4")
camion2=Camiones("Azul","Star","2019",150,300,14,6,2000)
camion2.getInfo()


