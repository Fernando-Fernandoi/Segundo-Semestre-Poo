class Animal:
    def __init__(self, tipo, edad, estado_salud):
        self.tipo = tipo
        self.edad = edad
        self.estado_salud = estado_salud

    def califica_revision_gratuita(self):
        if self.edad < 1 or (self.edad >= 10 and self.estado_salud.lower() == "malo"):
            return True
        return False


def gestionar_chequeo_veterinaria():
    try:
        cantidad = int(input("Ingrese la cantidad de animales a registrar: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return

        animales = []
        gratuitos = 0

        for i in range(cantidad):
            print(f"\nRegistro del animal {i + 1}:")
            tipo = input("Tipo de animal: ").strip()
            edad = int(input("Edad del animal (en años): "))
            estado_salud = input("Estado de salud (bueno/regular/malo): ").strip().lower()
            
            if estado_salud not in {"bueno", "regular", "malo"}:
                print("Estado de salud inválido. Intente de nuevo.")
                return

            animal = Animal(tipo, edad, estado_salud)
            animales.append(animal)

            if animal.califica_revision_gratuita():
                gratuitos += 1

        pagos = cantidad - gratuitos
        print("\nResumen del chequeo:")
        print(f"Animales que califican para revisión gratuita: {gratuitos}")
        print(f"Animales que deben pagar por la revisión: {pagos}")

    except ValueError:
        print("Entrada inválida. Por favor, ingrese valores numéricos donde se requiera.")


# Ejecución del programa
gestionar_chequeo_veterinaria()
