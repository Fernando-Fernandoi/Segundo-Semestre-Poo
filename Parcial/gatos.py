"""PROGRAMACIÓN ORIENTADA A OBJETOS
Parcial N°1
Docente: Víctor Saldivia Vera - Email: victor.saldivia@ulagos.cl
Ingeniería Civil enInformática - Departamento de Ciencias de la Ingeniería
Lunes 21 de Octubre de 2024
Enunciado
Resolver el siguiente ejercicio propuesto utilizando los conocimientos adquiridos en la primera y
segunda Unidad de POO. Se solicita desarrollar la solución utilizando Python. No se puede utilizar
apuntes, o códigos anteriores. El ejercicio tiene una ponderación de 100 puntos. Tiempo para
resolver el laboratorio: 90 minutos.
1. Eres el responsable de diseñar un sistema
que permita gestionar un Café de Gatos, un
lugar donde los clientes pueden disfrutar de
su café mientras interactúan con los gatos del
lugar. Cada gato en el café tiene su propio
espacio, y tú eres responsable de gestionar
tanto el bienestar de los gatos como el
inventario de productos necesarios para su
cuidado. Además, debes controlar el uso de
recursos como alimentos y juguetes para los
gatos.
Instrucciones
Gestión de Gatos en el Café (40 Puntos)
Los gatos son los protagonistas del café y cada
uno tiene características y necesidades únicas.
Piensa en cómo representarías a los gatos
dentro del sistema.
1. ¿Cómo representarías a los gatos dentro del sistema?
a. ¿Qué atributos crees que serían importantes para describir a un gato? Piensa en
atributos como el nombre, la edad, el nivel de energía y el nivel de hambre.
b. ¿Cómo se encapsulan estos atributos para evitar que otras partes del programa
puedan modificarlos directamente?
2. Métodos que necesita la clase Gato:
a. ¿Cómo diseñarías un método que permita que los gatos jueguen y cómo impactaría
esto en sus niveles de energía y hambre?
b. ¿Cómo diseñarías un método que permita alimentar a los gatos y restaurar sus
niveles de energía?
Programación Orientada a Objetos Parcial N°1
3. Método Mágico:
a. Implementa un método que te permita imprimir de forma clara el estado del gato.
¿Qué información incluirías en la representación del gato?
Gestión de Espacios en el Café (20 Puntos)
El café tiene diferentes áreas donde los gatos pueden estar. Imagina cómo organizarías estas áreas
dentro del sistema.
1. ¿Cómo representarías las áreas dentro del café?
a. ¿Qué atributos serían importantes para describir un área del café? Piensa en
atributos como el nombre del área, la capacidad máxima de gatos que puede
albergar, y una lista de los gatos presentes.
2. Métodos que necesita la clase Area:
a. ¿Cómo diseñarías un método que permita agregar un gato a un área? Debes
asegurarte de que no se exceda la capacidad máxima del área.
b. ¿Cómo diseñarías un método que permita listar los gatos presentes en el área?
Inventario del Café (20 Puntos)
El café necesita mantener un inventario de productos, como alimentos y juguetes, para el cuidado
de los gatos. Piensa en cómo podrías gestionar estos recursos dentro del sistema.
1. ¿Cómo representarías el inventario del café?
○ ¿Qué atributos serían importantes para describir el inventario? ¿Cómo
representarías los productos y la cantidad disponible de cada uno?
2. Métodos que necesita la clase Inventario:
○ ¿Cómo diseñarías un método que permita agregar productos al inventario y
controlar las cantidades?
○ ¿Cómo diseñarías un método que permita utilizar productos del inventario, donde se
debe asegurar de que no se usen más productos de los que están disponibles?
Estado de los Gatos e Interacción entre Clases (20 Puntos)
Cada gato tiene diferentes estados (hambriento, con energía, cansado). Piensa en cómo representar
estos estados dentro del sistema y cómo cambiarían dependiendo de sus acciones (jugar, comer,
descansar).
1. ¿Cómo podrías usar un método mágico para imprimir el estado de un gato?
a. ¿Qué información incluirías en la representación del gato? Piensa en el nombre, la
edad, el nivel de energía y el nivel de hambre.
b. ¿Cómo actualizarías estos valores a medida que el gato interactúa con el entorno
(juega, come, etc)?
2. Métodos de interacción entre las clases:
a. ¿Cómo permitirías que los gatos interactúen con el inventario, como por ejemplo
consumir alimentos o juguetes?
b. ¿Cómo gestionarías la adición de gatos a las áreas, asegurándote de que el sistema
se mantenga organizado?
Programación Orientada a Objetos Parcial N°1
Instrucciones Generales
● Crear un nuevo archivo Python (.py) para el ejercicio.
● Ejecutar el archivo y asegurarse de que los resultados mostrados en pantalla sean correctos.
● Comentar el código para explicar cada paso y operación realizada.
● Subir el archivo de Python (.py) en la plataforma Ulagos Virtual.
● Este código debe estar en los repositorios correspondientes de GitHub.
Programación Orientada a Objetos Parcial N°1"""

# Se crea una clase gato para poder dar nombre y utilizar estos mismos

class Gato:

# Se le definen nombre edad energia y hambre para usar luego

    def __init__(self, nombre, edad, energia, hambre):

        self.nombre = nombre

        self.edad = edad

        self.energia = energia

        self.hambre = hambre

# Se crea una clase area como ubicacion para los gatos

class Area:

# Se le definen nombre y capacidad

    def __init__(self, nombre, capacidad_maxima):

        self.nombre = nombre

        self.capacidad_maxima = capacidad_maxima

        self.gatos = []

# Se crea la clase inventario para ser usada con los gatos

class Inventario:

    def __init__(self):

        self.productos = {}


# Creación de las cosas y print de informacion respectiva

pepe = Gato(nombre="Pepe", edad=2, energia=100, hambre=100)

antonia = Gato(nombre="Antonia", edad=3, energia=100, hambre=100)

tony = Gato(nombre="Tony", edad=4, energia=100, hambre=100)

garfield = Gato(nombre="Garfield", edad=1, energia=100, hambre=100)

terraza = Area(nombre="Terraza", capacidad_maxima=2)

areaprincipal = Area(nombre="Area principal", capacidad_maxima=2)

terraza.gatos.append(pepe)

terraza.gatos.append(antonia)

areaprincipal.gatos.append(tony)

areaprincipal.gatos.append(garfield)

inventario = Inventario()

inventario.productos["comida"] = 100

inventario.productos["juguetes"] = 50

print(f"Área: {terraza.nombre}, Gato: {terraza.gatos[0].nombre}")

print(f"Área: {terraza.nombre}, Gato: {terraza.gatos[1].nombre}")

print(f"Área: {areaprincipal.nombre}, Gato: {areaprincipal.gatos[0].nombre}")

print(f"Área: {areaprincipal.nombre}, Gato: {areaprincipal.gatos[1].nombre}")

print(f"Gato: {pepe.nombre}, Energía: {pepe.energia}, Hambre: {pepe.hambre}")

print(f"Gato: {garfield.nombre}, Energía: {garfield.energia}, Hambre: {garfield.hambre}")

print(f"Inventario: {len(inventario.productos)} productos")