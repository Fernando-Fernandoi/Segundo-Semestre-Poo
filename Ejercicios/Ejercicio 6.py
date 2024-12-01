# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Velocidad máxima: {self.velocidad_maxima} km/h")

    def conducir(self):
        print(f"Conduciendo el vehículo {self.modelo} a {self.velocidad_maxima} km/h.")

# Clase Terrestre
class Terrestre:
    def __init__(self, ruedas):
        self.ruedas = ruedas

    def conducir_en_terreno(self):
        print(f"Conduciendo sobre {self.ruedas} ruedas en terreno terrestre.")

# Clase Acuatico
class Acuatico:
    def __init__(self, capacidad_agua):
        self.capacidad_agua = capacidad_agua

    def navegar_en_agua(self):
        print(f"Navegando con una capacidad de {self.capacidad_agua} litros de agua.")

# Clase Aereo
class Aereo:
    def __init__(self, altitud_maxima):
        self.altitud_maxima = altitud_maxima

    def volar(self):
        print(f"Volando a una altitud máxima de {self.altitud_maxima} metros.")

# Clase VehiculoHibrido que utiliza herencia múltiple
class VehiculoHibrido(Vehiculo, Terrestre, Acuatico, Aereo):
    def __init__(self, marca, modelo, velocidad_maxima, ruedas, capacidad_agua, altitud_maxima):
        Vehiculo.__init__(self, marca, modelo, velocidad_maxima)
        Terrestre.__init__(self, ruedas)
        Acuatico.__init__(self, capacidad_agua)
        Aereo.__init__(self, altitud_maxima)

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Ruedas: {self.ruedas}, Capacidad de agua: {self.capacidad_agua} litros, Altitud máxima: {self.altitud_maxima} metros")

    def conducir(self):
        super().conducir()
        self.conducir_en_terreno()
        self.navegar_en_agua()
        self.volar()

# Instanciación de vehículos híbridos
vehiculo_terrestre = Vehiculo("Ford", "Mustang", 250)
vehiculo_terrestre.mostrar_informacion()
vehiculo_terrestre.conducir()

print("\nVehículo Híbrido:")
vehiculo_hibrido = VehiculoHibrido("Tesla", "CyberTruck", 220, 4, 1000, 5000)
vehiculo_hibrido.mostrar_informacion()
vehiculo_hibrido.conducir()
