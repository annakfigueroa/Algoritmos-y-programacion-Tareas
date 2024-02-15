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


 #ps, defensa
punticos_oponente = [100, 100]
punticos_jugador = [100, 100]

import random

def malicioso(ps,defensa):
    defensa = defensa-10
    if defensa<= 0:
        defensa = 1
    return ps,defensa
def placaje(ps,defensa):
    ps -=35*100/defensa
    return ps,defensa
def ascuas (ps,defensa):
    ps -=20
    return ps,defensa
def látigo (ps,defensa):
    defensa = defensa-10
    if defensa<= 0:
        defensa = 1
    return ps,defensa
def pistola_de_agua (ps, defensa):
    ps -=35*100/defensa
    return ps/defensa
def balazo (ps,defensa):
    ps-=30
    return ps, defensa
 
while punticos_jugador[0]>0 and punticos_oponente[0]>0:
    ataque_jugador = input("Ataque:  ")
    if ataque_jugador== 'malicioso':
            print ("La defensa del oponente ha bajado")
            punticos_oponente = malicioso(punticos_oponente[0], punticos_oponente[1])
            if punticos_oponente[1]<=0:
                punticos_oponente = punticos_oponente[0], 1
    elif ataque_jugador =='placaje': 
            punticos_oponente =placaje(punticos_oponente[0], punticos_oponente[1])
            print ("Los puntos de vida del oponente han bajado")
    elif ataque_jugador=='ascuas':
            print ("Los puntos de vida del oponente han bajado")
            punticos_oponente = ascuas(punticos_oponente[0], punticos_oponente[1])
    else:
        print("Qué estás haciendo? tus ataques son placaje, malicioso y ascuas")
    
    ataque_oponente = random.randrange (1,3+1)
    if ataque_oponente==1: #latigo
            print ("Defensa oponente: latigo")
            print('Tu defensa ha bajado')
            punticos_jugador = látigo(punticos_jugador[0], punticos_jugador[1])
            if punticos_jugador[1]<=0:
                    punticos_jugador = punticos_oponente[0], 1
    elif ataque_oponente==2: #pistola de agua
            punticos_jugador= pistola_de_agua(punticos_jugador[0], punticos_jugador[1])
            print ("Defensa oponente: pistola de agua")
            print('Tus puntos de vida han bajado')
    elif ataque_oponente==3: #balazo
            punticos_jugador=balazo(punticos_jugador[0], punticos_jugador[1])
            print ("Defensa oponente: balazo")
            print('Tus puntos de vida han bajado')

if punticos_jugador[0]==0:
    print ("Lo siento, has perdido")
if punticos_oponente[0] ==0:
    print ("Felicidades, has ganado")
elif punticos_oponente[0]==0 and punticos_jugador[0]==0:
    print ("empate")
