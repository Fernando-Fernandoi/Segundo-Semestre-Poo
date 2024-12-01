#GUIA RÁPIDA DE CLASES EN PYTHON
#Docente: Victor Saldivia Vera - Institución: Universidad de Los Lagos

class Persona():
    
    # Constructort de Clase
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    # Atributos (Características compartidas por todos los objetos de la clase)
    # nombre = "Cristina"
    # apellido = "Torres"
    # edad = 23
    
    #Métodos (Comportamientos)
    
    def hablar(self):
        print(f"{self.nombre} esta hablando")
        
    def caminar(self):
        print(f"{self.nombre} esta caminando")
        
        
persona1 = Persona("Cristina", "Torres", 23)
persona2 = Persona("Benjamin", "Gomez", 20)


print(f"{persona1.nombre}")
print(f"{persona1.apellido}")
print(f"{persona1.edad}")

persona1.hablar()
persona2.caminar()
        