#Resolvente
import math

a=int(input("Introduce el valor de a: "))
b=int(input("Introduce el valor de b: "))
c=int(input("Introduce el valor de c: "))

raíz_1= (int(b)**2)
raíz_2 = math.sqrt (raíz_1 - ((int(4*a*c))))
if raíz_2>=0:
    numerador = (int(-(b))) + (raíz_2)
    denominador = (int(2*a))
    resultado_1=int((numerador)/(denominador))


raíz_3= (int(b)**2)
raíz_4 =math.sqrt (raíz_3 - ((int(4*a*c))))
if raíz_4>=0:
    numerador_2 = (int(-(b))) - (raíz_4)
    denominador_2 = (int(2*a))
    resultado_2=int((numerador_2)/(denominador_2))
print("Tus posibles soluciones son:")
print ("x1= ")
print (resultado_1)
if raíz_2<0:
    print ("No tiene solución real")
print ("x2= ")
print (resultado_2)
if raíz_4<0:
    print ("No tiene solución real")