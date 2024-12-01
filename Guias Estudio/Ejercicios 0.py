class Estudiante:
    def __init__(self, nombre, promedio):
        self.__nombre = nombre
        self.__promedio = promedio
        self.estado = self.evaluar_estado()

    def actualizar_promedio(self, nuevo_promedio):
        self.__promedio = nuevo_promedio
        self.estado = self.evaluar_estado()

    def evaluar_estado(self):
        return self.__promedio >= 4.0

    def __str__(self):
        estado_texto = "Aprobado" if self.estado else "Reprobado"
        return f"Nombre: {self.__nombre}, Promedio: {self.__promedio}, Estado: {estado_texto}"


# Ejemplo de uso
estudiantes = [
    Estudiante("Ana", 4.5),
    Estudiante("Luis", 3.8),
    Estudiante("Carla", 4.2)
]

for estudiante in estudiantes:
    print(estudiante)
