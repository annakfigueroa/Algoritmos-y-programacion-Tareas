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



PS_jugador = 100 #puntos de salud del jugador
PS_oponente = 100 #puntos de salud del oponente
defensa_oponente = 100
defensa_jugador = 100
import random

options = {
    "malicioso":1, 
    "placaje":2 , 
    "ascuas":3
    }
 
while PS_oponente >0 and PS_jugador>0: 
    ataque_jugador = input("Ataque:  ")
    while not ataque_jugador: ""
    if ataque_jugador=="malicioso":
            print ("La defensa del oponente ha bajado")
            defensa_oponente = defensa_oponente - 10
            if defensa_oponente <= 0:
                defensa_oponente = 1
    elif ataque_jugador =="placaje":
            PS_oponente-=35 * (100/defensa_oponente)
            print ("La defensa del oponente ha bajado")
    elif ataque_jugador=="ascuas":
            print ("La defensa del oponente ha bajado")
            PS_oponente-=20
    else:
        print("Qué estás haciendo? tus ataques son",options)
    
    ataque_oponente = random.randrange (1,3+1)
    if ataque_oponente==1: #latigo
            defensa_jugador -= 10
            if defensa_jugador <= 0:
                defensa_jugador = 1
            print ("Defensa oponente: latigo")
            print('Tu defensa ha bajado')
    elif ataque_oponente==2: #pistola de agua
            PS_jugador-=35 * (100/defensa_jugador)
            print ("Defensa oponente: pistola de agua")
            print('Tu defensa ha bajado')

    elif ataque_oponente==3: #balazo
            PS_jugador-=20
            print ("Defensa oponente: balazo")
            print('Tu defensa ha bajado')

if PS_jugador<=0:
    print ("Lo siento, has perdido")
if PS_oponente <=0:
    print ("Felicidades, has ganado")
elif PS_oponente<=0 and PS_jugador<=0:
    print ("empate")
