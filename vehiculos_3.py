#Programa de concesionario de vehículos, se determina el concesionario que vende cada carro

class Seller:
    def __init__(self, nombre, concesionario, id, age):
        self.nombre=nombre
        self.concesionario=concesionario
        self.id=id
        self.age=age
class Vehicle:
    def __init__(self,type,brand,color,place):
        self.type=type
        self.brand=brand
        self.color=color
        self.place=place
class Car(Vehicle):
    def __init__(self,type,brand,color,place,year,plate,vendedor=None):
        super().__init__(type,brand,color,place)
        self.year=year
        self.plate=plate
        self.vendedor=vendedor
    def __str__(self): 
        return "Tipo de Vehículo:{}, Marca: {}, Color: {}, Lugar de registro: {}, Año de registro: {}, Placa: {}, Vendedor: {}".format(self.type, self.brand, self.color, self.place,self.year,self.plate,self.vendedor.concesionario if self.vendedor else 'Sin vendedor') 
class Boat(Vehicle):
    def __init__(self,type,brand,color,place,nameb,typeb,vendedor=None):
        super().__init__(type,brand,color,place)
        self.nameb=nameb
        self.typeb=typeb
        self.vendedor=vendedor
    def __str__(self):
        return "Tipo de Vehículo:{}, Marca: {}, Color: {}, Lugar de registro: {}, Nombre del barco: {},Tipo de barco: {}, Vendedor: {}".format(self.type, self.brand, self.color, self.place,self.nameb,self.typeb,self.vendedor.concesionario if self.vendedor else 'Sin vendedor')
class Plane(Vehicle):
    def __init__(self,type,brand,color,place,vlicense,pilotlicense,vendedor=None):
        super().__init__(type,brand,color,place)
        self.vlicense=vlicense
        self.pilotlicense=pilotlicense
        self.vendedor=vendedor
    def __str__(self):
        return "Tipo de Vehículo:{}, Marca: {}, Color: {}, Lugar de registro: {}, Licencia: {}, Licencia piloto: {}, Vendedor: {}".format(self.type, self.brand, self.color, self.place,self.vlicense,self.pilotlicense,self.vendedor.concesionario if self.vendedor else 'Sin vendedor')
def registro_principal(vehiculo,vendedor):
    vehiculo.vendedor=vendedor 
    print(f"¡Venta registrada!\n{vehiculo} ahora es vendido por {vendedor.nombre}")

vendedor1 = Seller("Juan Perez","Concesionario del Sur", "123456789", "47")
vendedor2 = Seller("Pedro Gonzalez","Concesionario del Norte", "987654321", "58")

corolla=Car("Carro","Toyota","Plateado","Merida",2009,"A9876YH",vendedor1)
supra=Car("Carro","Toyota","Naranja","Maracaibo",1998,"Y9KASDN")

perlanegra=Boat("Bote","Pirate","Marron","Caribe","Perla Negra","Galeón",vendedor2)
yaterandom=Boat("Bote","Oceanco","Blanco","Trinidad y Tobago","Octopus","Yate")

avion1=Plane("Avión","Airbus","Azul","Caracas","YT123",389898)
avion2=Plane("Avión","Boeing","Verde","Táchira","AB897",908391,vendedor2)
print("-->Vehículos disponibles:")
for i in [corolla, supra, perlanegra,yaterandom,avion1,avion2]:
    print(f"-{i}")

    
