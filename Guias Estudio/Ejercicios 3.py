class Planta:
    def __init__(self, tipo, agua_necesaria):
        self.__tipo = tipo
        self.__estado = "Semilla"
        self.__agua_necesaria = agua_necesaria

    def regar(self, agua):
        if agua >= self.__agua_necesaria:
            self.__estado = "Creciendo"
            return "Planta regada y creciendo."
        return "Agua insuficiente."

    def __str__(self):
        return f"Planta tipo: {self.__tipo}, Estado: {self.__estado}, Agua necesaria: {self.__agua_necesaria}L."


class Area:
    def __init__(self, nombre):
        self.nombre = nombre
        self.plantas = []

    def añadir_planta(self, planta):
        self.plantas.append(planta)

    def listar_plantas(self):
        return "\n".join(str(planta) for planta in self.plantas)
