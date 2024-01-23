año = int(input("Escribe un año entre 1900 y 2199 "))
if año<1900 or año>2199:
    print ("Este año no entra dentro del rango")
año = int(input("Escribe un año entre 1900 y 2199 "))
if año %4==0: 
    if int(año) %100== 0 or int (año) %400 !=0: 
        print ("El año",año, "es bisiesto")
        print ("Existen",int((año-1900)//4),
               "años bisiestos desde 1900")
else:
    print ("El año no es bisiesto")