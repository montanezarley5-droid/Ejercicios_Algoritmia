#nombres: programa para la medididas de los triangulos

#entradas
#lado 1: se solicita la medida del primer triangulo
#lado 2: se solicita la medida del segundo triangulo
#lado 3: se solicita la medida del tercer triangulo

#procesos
# se pide la medida de los triangulos

#salida
#medidas de los triangulos

print("Ingrese la medida del triangulo")
lado1=int(input("Lado 1: "))
lado2=int(input("Lado 2: "))
lado3=int(input("Lado 3: "))
if lado1==lado2 & lado2 == lado3:
    print("Es un triangulo equilatero")
elif lado1 == lado2 or lado2==lado3:
    print ("Es un triangulo isoseles")
else:
    print("Es un triangulo escaleno")