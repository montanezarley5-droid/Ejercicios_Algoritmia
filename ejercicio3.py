year = int(input("Ingrese el año"))
if(year % 4 == 0 and year % 100 !=  0) or (year % 400 == 0):
    print("año es bisiesto")
else:
    print("año no es bisiesto")