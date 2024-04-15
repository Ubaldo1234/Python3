class Vehiculo():
    def __init__(self,tipoVehiculo,marca,modelo,color,precio): #Constructor
        self.tipo = tipoVehiculo
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio



class Carro(Vehiculo):#herecia
    def Carro(self,tipoVehiculo,marca,modelo,color,precio):
        super().__init__(tipoVehiculo,marca,modelo,color,precio)

    def  Descripcion(self):
        txt = f"Tu Vehiculo tiene las siguientes caracteristicas:\n{self.tipo} {self.marca} {self.modelo} {self.color} {self.precio}"
        return  txt


class Avion(Vehiculo):
    def Avion(self, tipoVehiculo, marca, modelo, color, precio):
        super().__init__(tipoVehiculo, marca, modelo, color, precio)

    def Descripcion(self):
        txt = f"Tu Vehiculo tiene las siguientes caracteristicas:\n{self.tipo} {self.marca} {self.modelo} {self.color} {self.precio}"
        return txt


carro = Carro("Carro","ford","2020","negro",70000)
print(carro.Descripcion())
print()
avion = Avion("Avion","Airbus", "A330","blanco con azul",1000000)
print(avion.Descripcion())








