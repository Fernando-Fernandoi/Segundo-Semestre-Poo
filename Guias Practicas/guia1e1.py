#Ejercicio 1

'''Se solicita crear una clase ReservaHostal que permita a los usuarios crear reservas de
habitaciones en un hostal. Cada reserva tendrá atributos como el nombre del cliente, la fecha
de entrada, la fecha de salida, y el número de habitación. Implementar los siguientes
requerimientos:
Métodos:
● Un método para calcular la duración de la estadía del cliente.
● Un método mágico para mostrar la información de la reserva.
● Un método para cambiar la fecha de salida.
Se debe eliminar un objeto ReservaHostal, además de imprimir un mensaje indicando que la
reserva ha sido cancelada'''

class ReservaHostal:
    def __init__(self, nombre, habitacion, diaentrada, diasalida):
        self.nombre = nombre
        self.habitacion = habitacion
        self.diaentrada = diaentrada  
        self.diasalida = diasalida    

    def duracion(self):
        return self.diasalida - self.diaentrada

    def __str__(self):
        return (f"Se ha realizado una reserva de {self.nombre} para la habitación {self.habitacion}. "
                f"Fecha de entrada: {self.diaentrada}, "
                f"Fecha de salida: {self.diasalida}, "
                f"Duración: {self.duracion()} días.")

    def cambiosalida(self, nuevasalida):
        self.diasalida = nuevasalida

    def __del__(self):
        print(f"La reserva de {self.nombre} ha sido cancelada.")

diaentrada = 10
diasalida = 15
reserva = ReservaHostal("Pedro", 5, diaentrada, diasalida)
print(reserva)

duracion = reserva.duracion()
print(f"Duración de la estadía: {duracion} días.")

nuevasalida = 20
reserva.cambiosalida(nuevasalida)
print("Después de cambiar la fecha de salida:")
print(reserva)
del reserva

