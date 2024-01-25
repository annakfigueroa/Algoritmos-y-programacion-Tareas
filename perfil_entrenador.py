x = input ("Eres chico o chica?")
w = "Bienvenid"
if x == "chico":
    w += 'o'
else:
    w += 'a'
print(w,"al mundo de los pokemon!")

y = input("Que edad tienes? ")
if int(y)<10:
    if x=="chico":
        print("No tienes edad",
              "para ser entrenador")
    else:
        print("No tienes edad",
          "para ser entrenadora")
    quit()
    
reg = input("Necesitas un compañero de viaje ¿En qué región te encuentras? ")
if reg== "kanto":
    print ("Tu compañera de viaje es Misty!")
else:
    print ("Tu compañero de viaje es Brook!")

tipo = input("¿Qué tipo de Pokemon quieres para empezar? ")
if tipo == "fuego":
    print("Tu starter es Charmander")
elif tipo == "agua":
    print("Tu starter es Squirtle")
else:
    print("Tu starter es Bulbasaur")

print("¡Comienza la aventura!")