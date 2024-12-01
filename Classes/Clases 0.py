class Persona:
    nombre: "Cristina"
    apellido: "Torres"
    edad: 23
    def hablar(self):
        print(f"{self.nombre} esta hablando")
    def caminar(self):
        print(f"{self.nombre} esta caminando")
    def comer(self):
        print(f"{self.nombre} esta comendo")
    def dormir(self):
        print(f"{self.nombre} esta dormido")
    def estudiar(self):
        print(f"{self.nombre} esta estudiando")
persona1 = Persona()

print(f"Nombre: {persona1.nombre}")
print(f"Apellido: {persona1.apellido}")
print(f"Edad: {persona1.edad} años")

persona1.hablar
persona1.caminar
persona1.comer
persona1.dormir
persona1.estudiar