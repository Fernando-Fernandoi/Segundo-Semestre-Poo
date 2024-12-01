"""Enunciado
Resolver los dos ejercicios propuestos a continuación utilizando los conocimientos adquiridos en la
primera Unidad de POO. Se solicita desarrollar la solución utilizando Python y Pygame. No se puede
utilizar apuntes, o códigos anteriores. Cada ejercicio tiene una ponderación de 50 puntos. Tiempo
para resolver el laboratorio: 90 minutos.
1. Implementar un sistema básico para gestionar personajes de un
videojuego utilizando programación orientada a objetos.
Cada personaje tendrá un nombre, nivel de vida y puntos de ataque. La
idea es que los personajes puedan interactuar entre ellos, permitiendo
que un personaje ataque a otro, lo que disminuirá su vida. Además,
deberás verificar si un personaje está vivo o no.
Requerimientos:
1. Clase Personaje:
○ Atributos: el nombre del personaje, el nivel de vida del personaje y los
puntos de ataque del personaje.
○ Métodos: un método que permita que el personaje ataque a otro,
disminuyendo la vida del otro personaje según los puntos de ataque del
atacante. Un segundo método, que verifique si el personaje sigue vivo. Debe
devolver True si el nivel de vida es mayor a 0, y False si no. Por último
implementar un método mágico que permita devolver un string que muestre
el estado del personaje (nombre, vida, y ataque).
Instrucciones:
1. Implementar la clase Personaje con los atributos y métodos descritos
anteriormente.
2. Crear al menos dos personajes. Cada personaje debe tener un nombre, vida inicial y
puntos de ataque.
3. Simula un combate entre los personajes haciendo que uno ataque al otro. Después
de cada ataque, se debe mostrar el estado de ambos personajes.
4. Repetir los ataques hasta que uno de los personajes quede sin vida. Utiliza un
método para verificar si el personaje sigue en pie."""

# Se crean clases de personajes para la pelea y se define lo que se va a hacer.
class Personaje:
    def __init__(self, nombre):
    self.nombre = nombre
    self.vida = 1200
    self.ataque = 500

# Aqui se intenta colocar todas las mecanicas y lo pedido al personaje.
    def atacar(self, enemigo):
        enemigo.vida -= self.ataque
        print(f"{self.nombre} atacó a {enemigo.nombre} y causó {self.ataque} puntos de daño.")
        if enemigo.vida <= 0:
            print(f"{enemigo.nombre} ha muerto.")
            return True
    
    def verificar_vida(self):
        return self.vida > 0
    
    def __str__(self):
        return f"{self.nombre} tiene {self.vida} puntos de vida y {self.ataque} puntos de ataque."


# Aqui se crea el segundo personaje y se define lo que se va a hacer.
class Enemigo:
    self.nombre = nombre
    self.vida = 1500
    self.ataque = 400
    
    def atacar(self, jugador):
        jugador.vida -= self.ataque
        print(f"{self.nombre} atacó a {jugador.nombre} y causó {self.ataque} puntos de daño.")
        if jugador.vida <= 0:
            print(f"{jugador.nombre} ha muerto.")
            return True

# Aca se intento crear un verificador de personajes vivos y ataque.
def verificar_vida(personaje):
    if personaje.vida <= 0:
        print(f"{personaje.nombre} ha muerto.")
        return True

def ataque(atacante, defensor):
    defensor.vida -= atacante.ataque
    print(f"{atacante.nombre} atacó a {defensor.nombre} y causó {atacante.ataque} puntos de daño.")
    if defensor.vida <= 0:
        print(f"{defensor.nombre} ha muerto.")
        return True

# Se crean los personajes y se comienza la pelea
jugador = Personaje("Jugador 1", 1000, 300)
enemigo = Enemigo("Enemigo 1", 1500, 400)

while jugador.vida > 0 and enemigo.vida > 0:
    if ataque(jugador, enemigo):
        if ataque(enemigo, jugador):
            print(f"Jugador: {jugador.vida} puntos de vida")
            print(f"Enemigo: {enemigo.vida} puntos de vida")