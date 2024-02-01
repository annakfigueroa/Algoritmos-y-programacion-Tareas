x = input ("Eres chico o chica? ")
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
    
tuple_pokemones= ("Charmander", "Squirtle","Bulbasaur")
tipo = input("¿Qué tipo de Pokemon quieres para empezar? ")

if tipo == "fuego":
    print("Tu starter es {}".format (tuple_pokemones[0]))
elif tipo == "agua":
    print("Tu starter es {}".format (tuple_pokemones[1]))
else:
    print("Tu starter es {}".format (tuple_pokemones[2]))

print("¡Comienza la aventura!")


punticos_jugador = 100,100 #vida, defensa
punticos_oponente = 100,100

import random

options = {
    "atq1": (0,10, "malicioso"),
    "atq2": (35, 0, "placaje"),
    "atq3": (30, 0, "ascuas"),
    }
 
while punticos_jugador[0]>0 and punticos_oponente[0]>0: 
    ataque_jugador = input("Ataque:  ")
    while not ataque_jugador: ""
    if ataque_jugador== options["atq1"] [2]:
            print ("La defensa del oponente ha bajado")
            punticos_oponente = punticos_oponente[0], punticos_oponente[1] - options["atq1"][1]
            if punticos_oponente[1]<=0:
                punticos_oponente = punticos_oponente[0], 1
    elif ataque_jugador ==options["atq2"] [2]:
            punticos_oponente = punticos_oponente[0] - punticos_oponente["atq2"][0] * (100/punticos_oponente[1]), punticos_oponente[1]
            print ("La defensa del oponente ha bajado")
    elif ataque_jugador==options["atq3"] [2]:
            print ("La defensa del oponente ha bajado")
            punticos_oponente = punticos_oponente[0]-options ["atq3"][0], punticos_oponente[1]
    else:
        print("Qué estás haciendo? tus ataques son",options)
    
    ataque_oponente = random.randrange (1,3+1)
    if ataque_oponente==1: #latigo
            print ("Defensa oponente: latigo")
            print('Tu defensa ha bajado')
            punticos_jugador = punticos_jugador[0]-1, punticos_jugador[1]
            if punticos_jugador[1]<=0:
                    punticos_jugador = punticos_oponente[0], 1
    elif ataque_oponente==2: #pistola de agua
            punticos_jugador= punticos_jugador[0]-35 * (punticos_jugador[1]/100)
            print ("Defensa oponente: pistola de agua")
            print('Tu defensa ha bajado')

    elif ataque_oponente==3: #balazo
            punticos_jugador=punticos_jugador[0]-30, punticos_jugador[1]
            print ("Defensa oponente: balazo")
            print('Tu defensa ha bajado')

if punticos_jugador[0]<=0:
    punticos_jugador[0]=0, punticos_jugador[1]
    print ("Lo siento, has perdido")
if punticos_oponente[0] <=0:
    punticos_oponente[0]=0, punticos_oponente[1]
    print ("Felicidades, has ganado")
elif punticos_oponente[0]<=0 and punticos_jugador[0]<=0:
    print ("empate")
