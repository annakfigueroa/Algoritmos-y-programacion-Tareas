#Programa para registrar 3 tipos de vehículos: carros, botes y aviones
class Car:
    def __init__(self,tipo,brand,color,place,year,plate):
        self.tipo=tipo
        self.brand=brand
        self.color=color
        self.place=place
        self.year=year
        self.plate=plate
    def __str__(self):
        return "Tipo de Vehículo: {}, Marca: {}, Color: {}, Lugar de registro: {}, Año de registro: {}, Placa: {}".format(self.tipo, self.brand, self.color, self.place,self.year,self.plate) 
class Boat:
    def __init__(self,tipo,brand,color,place,nameb,typeb):
        self.tipo=tipo
        self.brand=brand
        self.color=color
        self.place=place
        self.nameb=nameb
        self.typeb=typeb
    def __str__(self):
        return "Tipo de Vehículo: {}, Marca: {}, Color: {}, Lugar de registro: {}, Nombre del barco: {},Tipo de barco: {}".format(self.tipo, self.brand, self.color, self.place,self.nameb,self.typeb)
class Plane:
    def __init__(self,tipo,brand,color,place,vlicense,pilotlicense):
        self.tipo=tipo
        self.brand=brand
        self.color=color
        self.place=place
        self.vlicense=vlicense
        self.pilotlicense=pilotlicense
    def __str__(self):
        return "Tipo de Vehículo: {}, Marca: {}, Color: {}, Lugar de registro: {}, Licencia: {}, Licencia piloto: {}".format(self.tipo, self.brand, self.color, self.place,self.vlicense,self.pilotlicense)

corolla=Car("Carro","Toyota","Plateado","Merida",2009,"A9876YH")
supra=Car("Carro","Toyota","Naranja","Maracaibo",1998,"Y9KASDN")

perlanegra=Boat("Bote","Pirate","Marron","Caribe","Perla Negra","Galeón")
yaterandom=Boat("Bote","Oceanco","Blanco","Trinidad y Tobago","Octopus","Yate")

avion1=Plane("Avión","Airbus","Azul","Caracas","YT123",389898)
avion2=Plane("Avión","Boeing","Verde","Táchira","AB897",908391)
print("--> Carros")
print(corolla)
print(supra)
print()
print("-->Botes")
print(perlanegra)
print(yaterandom)
print()
print("-->Aviones")
print(avion1)
print(avion2)