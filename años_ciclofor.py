año = int(input("Escribe un año entre 1900 y 2199 "))
def bisiesto(año):
	return año % 4==0 and (año % 100==0 or not año % 400==0)

for año in range(1900, año):
	if bisiesto(año):
            print(año, end=' ')

print (": son los años bisiestos entre 1900 y",año+1,)