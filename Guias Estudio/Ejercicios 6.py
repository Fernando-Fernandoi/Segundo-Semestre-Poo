class SuscripcionGimnasio:
    descuento_anual = 0.15  # Descuento para suscripciones anuales, variable de clase

    def __init__(self, nombre_cliente, tipo_suscripcion, costo):
        self._nombre_cliente = nombre_cliente
        self._tipo_suscripcion = tipo_suscripcion
        self._costo = costo

    @property
    def nombre_cliente(self):
        return self._nombre_cliente

    @nombre_cliente.setter
    def nombre_cliente(self, nombre_cliente):
        self._nombre_cliente = nombre_cliente

    @property
    def tipo_suscripcion(self):
        return self._tipo_suscripcion

    @tipo_suscripcion.setter
    def tipo_suscripcion(self, tipo_suscripcion):
        self._tipo_suscripcion = tipo_suscripcion

    @property
    def costo(self):
        return self._costo

    @costo.setter
    def costo(self, costo):
        if costo < 0:
            raise ValueError("El costo no puede ser negativo")
        self._costo = costo

    def calcular_costo_final(self):
        """Calcula el costo final de la suscripción, aplicando el descuento si es anual."""
        if self._tipo_suscripcion == "Anual":
            return self._costo * (1 - SuscripcionGimnasio.descuento_anual)
        return self._costo

    @staticmethod
    def calcular_costo_con_descuento_bienvenida(costo, descuento):
        """Calcula el costo con un descuento de bienvenida."""
        return costo * (1 - descuento)


# Uso de la clase SuscripcionGimnasio
cliente1 = SuscripcionGimnasio("Carlos", "Anual", 100000)
cliente2 = SuscripcionGimnasio("Ana", "Mensual", 30000)

print(f"{cliente1.nombre_cliente} tiene un costo final: ${cliente1.calcular_costo_final()}")
print(f"{cliente2.nombre_cliente} tiene un costo final: ${cliente2.calcular_costo_final()}")
