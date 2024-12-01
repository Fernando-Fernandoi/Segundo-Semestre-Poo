class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def hacer_sonido(self):
        print(f"El animal {self.nombre} hace un sonido.")

class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.raza = raza

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Peso: {self.peso} kg, Raza: {self.raza}")

class Gato(Animal):
    def __init__(self, nombre, edad, peso, color):
        super().__init__(nombre, edad, peso)
        self.color = color

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Peso: {self.peso} kg, Color: {self.color}")

class Pajaro(Animal):
    def __init__(self, nombre, edad, peso, especie):
        super().__init__(nombre, edad, peso)
        self.especie = especie

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Pío!")

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Peso: {self.peso} kg, Especie: {self.especie}")

class Pez(Animal):
    def __init__(self, nombre, edad, peso, tipo_agua):
        super().__init__(nombre, edad, peso)
        self.tipo_agua = tipo_agua

    def hacer_sonido(self):
        print(f"{self.nombre} hace burbujeas.")

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Peso: {self.peso} kg, Tipo de agua: {self.tipo_agua}")

perro = Perro("Rex", 5, 10, "Pastor Alemán")
gato = Gato("Miau", 3, 4, "Gris")
pajaro = Pajaro("Pío", 1, 0.2, "Canario")
pez = Pez("Burbuja", 2, 0.5, "Agua dulce")

perro.hacer_sonido()
gato.hacer_sonido()
pajaro.hacer_sonido()
pez.hacer_sonido()

print("\nDatos del Perro:")
perro.mostrar_datos()

print("\nDatos del Gato:")
gato.mostrar_datos()

print("\nDatos del Pájaro:")
pajaro.mostrar_datos()

print("\nDatos del Pez:")
pez.mostrar_datos()
