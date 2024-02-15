class Vehicles:
    registro = 'Registro de Vehículos'
    def __init__(self,type,brand,color,place):
        self.type=type
        self.brand=brand
        self.color=color
        self.place=place
class Car(Vehicles):
    def __init__(self,type,brand,color,place,year,plate):
        super().__init__(type,brand,color,place)
        self.year=year
        self.plate=plate
    def carrito(self): 
        return "Tipo de Vehículo:{}, Marca: {}, Color: {}, Lugar de registro: {}, Año de registro: {}, Placa: {}".format(self.type, self.brand, self.color, self.place,self.year,self.plate) 
class Boat(Vehicles):
    def __init__(self,type,brand,color,place,nameb,typeb):
        super().__init__(type,brand,color,place)
        self.nameb=nameb
        self.typeb=typeb
    def bote(self):
        return "Tipo de Vehículo:{}, Marca: {}, Color: {}, Lugar de registro: {}, Nombre del barco{},Tipo de barco: {}".format(self.type, self.brand, self.color, self.place,self.nameb,self.typeb)
class Plane(Vehicles):
    def __init__(self,type,brand,color,place,vlicense,pilotlicense):
        super().__init__(type,brand,color,place)
        self.vlicense=vlicense
        self.pilotlicense=pilotlicense
    def volar(self):
        return "Tipo de Vehículo:{}, Marca: {}, Color: {}, Lugar de registro: {}, Licencia: {}, Licencia piloto: {}".format(self.type, self.brand, self.color, self.place,self.vlicense,self.pilotlicense)

corolla=Car("Carro","Toyota","Plateado","Merida",2009,"A9876YH")
supra=Car("Carro","Toyota","Naranja","Maracaibo",1998,"Y9KASDN")
perlanegra=Boat("Bote","Pirate","Marron","Caribe","Perla Negra","Galeón")
yaterandom=Boat("Bote","Oceanco","Blanco","Trinidad y Tobago","Octopus","Yate")
avion1=Plane("Avión","Airbus","Azul","Caracas","YT123",389898)
avion2=Plane("Avión","Boeing","Verde","Táchira","AB897",908394-1)
print("--> Carros")
print(corolla.carrito())
print(supra.carrito())
print()
print("-->Botes")
print(perlanegra.bote())
print(yaterandom.bote())
print()
print("-->Aviones")
print(avion1.volar())
print(avion2.volar())

