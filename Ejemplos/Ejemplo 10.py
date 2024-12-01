class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def comer(self):
        print(f"{self.nombre} está comiendo.")
class Perro(Animal):
    def __innit__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
    def ladrar(self):
        print(f"{self.nombre} está ladrando.")
class Gato(Animal):
    def __init__(self, nombre, edad, color_pelaje):
        super().__init__(nombre, edad)
        self.color_pelaje = color_pelaje
    def maullar(self):
        print(f"{self.nombre} está maullando.")