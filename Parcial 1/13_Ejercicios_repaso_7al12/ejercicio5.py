"""5.- 
Crear una lista y un diccionario con el contenido de esta tabla: 

  ACCION              TERROR        DEPORTES
  MAXIMA VELOCIDAD    LA MONJA       ESPN
  ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
  RAPIDO Y FURIOSO I  LA MALDICION   ACCION"""

datos = [
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]

datos_dict = {
    "ACCION": [],
    "TERROR": [],
    "DEPORTES": []
}

for fila in datos:
    datos_dict["ACCION"].append(fila[0])
    datos_dict["TERROR"].append(fila[1])
    datos_dict["DEPORTES"].append(fila[2])

print("Lista:")
for fila in datos:
    print(fila)

print("\nDiccionario:")
for categoria, valores in datos_dict.items():
    print(categoria + ":", valores)
