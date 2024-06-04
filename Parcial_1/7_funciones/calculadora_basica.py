#hacer una calculadora que seleccione la operacion


"""from optparse import Option


print("SUMA")
print("RESTA")
print("MULTIPLICACION")
print("DIVISION")

opcion = input("Eliga una opcion:").upper()

opcion=True
while opcion:
 
 if opcion=="1" or opcion=="+" or opcion=="SUMA":
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2:"))
    suma=n1+n2
    print(f"(n1)+(n2)=(suma)")

 elif opcion=="2" or opcion=="-" or opcion=="RESTA":
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2:"))
    resta=n1-n2
    print(f"(n1)-(n2)=(resta)")
 
 elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2:"))
    multiplicacion=n1*n2
    print(f"(n1)*(n2)=(multiplicacion)")
 
 elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2:"))
    multiplicacion=n1/n2
    print(f"(n1)/(n2)=(division)")    
 else:
    print("Terminaste la ejecucion de SW")    
    opcion=False"""

opcion = input("Eliga una opcion:").upper()

def solicitarNumeros():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))

def operacionAritmetica(num1,num2,ope):    
     if opcion=="1" or opcion=="+" or opcion=="SUMA":
      return f"(n1)+(n2)=(n1+n2)"
     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
      return f"(n1)-(n2)=(n1-n2)"
     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
      return f"(n1)*(n2)=(n1*n2)"
     elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
      return f"(n1)/(n2)=(n1/n2)"   
     else:
      return"Terminaste la ejecucion de SW"     
   