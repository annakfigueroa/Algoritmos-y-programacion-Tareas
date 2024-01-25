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

tipo = input("¿Qué tipo de Pokemon quieres para empezar? ")
if tipo == "fuego":
    print("Tu starter es Charmander")
elif tipo == "agua":
    print("Tu starter es Squirtle")
else:
    print("Tu starter es Bulbasaur")

print("¡Comienza la aventura!")

PS_jugador = 100 #puntos de salud del jugador
PS_oponente = 100 #puntos de salud del oponente
defensa_oponente = 100
defensa_jugador = 100
import random

options = ["malicioso" , "placaje" , "ascuas"]
 
while PS_oponente >0 and PS_jugador>0: 
    ataque_jugador = input("Ataque:  ")
    while not ataque_jugador: ""
    if ataque_jugador==options[0]:
            PS_oponente-= 10 
    elif ataque_jugador ==options[1]:
            PS_oponente-=35 
    elif ataque_jugador==options[2]:
            PS_oponente-=20
    else:
        print("Qué estás haciendo? tus ataques son",options)
    
    ataque_oponente = random.randrange (1,3+1)
    if ataque_oponente==1: #latigo
            PS_jugador -= 10
            print ("Defensa: latigo")
    elif ataque_oponente==2: #pistola de agua
            PS_jugador-=35 
            print ("Defensa: pistola de agua")
    elif ataque_oponente==3: #balazo
            PS_jugador-=20
            print ("Defensa: balazo")
if PS_jugador<=0:
    print ("Lo siento, has perdido")
if PS_oponente <=0:
    print ("Felicidades, has ganado")
elif PS_oponente<=0 and PS_jugador<=0:
    print ("empate")
