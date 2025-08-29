#nombre: progama verificacion si un numero es positivo o negativo

#entrada
#ingresa el numero para saber si es positivo 
#ingresa el numero para saber si es negativo

numer = int(input("Ingrese el numero: "))
if numer < 0:
 print ("el numero es negativo")
elif numer == 0:
  print("el numero es cero")
else:
 print("el numero es positivo")
