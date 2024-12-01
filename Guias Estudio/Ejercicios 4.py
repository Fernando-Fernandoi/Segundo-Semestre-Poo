class SistemaVentaTickets:
    descuento_grupo = 0.20  # Descuento por compras en grupo, variable de clase
    
    def __init__(self):
        self._menu_tickets = {}  # Diccionario para almacenar tipos de tickets y su precio
        self._ventas = []  # Lista para almacenar las ventas registradas

    def agregar_ticket(self, tipo, precio):
        """Agrega un tipo de ticket al sistema. El precio debe ser positivo."""
        assert precio > 0, "El precio del ticket debe ser positivo"
        self._menu_tickets[tipo] = precio

    def registrar_venta(self, tipo, cantidad):
        """Registra la venta de un ticket. Asegura que el ticket exista en el menú."""
        assert tipo in self._menu_tickets, f"El tipo de ticket {tipo} no existe en el menú."
        precio_unitario = self._menu_tickets[tipo]
        total_venta = self.calcular_total_venta(precio_unitario, cantidad)
        self._ventas.append((tipo, cantidad, total_venta))
        return total_venta

    @staticmethod
    def calcular_total_venta(precio, cantidad):
        """Calcula el total de la venta aplicando el descuento por compras en grupo."""
        total = precio * cantidad
        return total * (1 - SistemaVentaTickets.descuento_grupo)

    def obtener_ventas(self):
        """Devuelve las ventas registradas."""
        return self._ventas


# Uso del sistema de venta de tickets
sistema = SistemaVentaTickets()
sistema.agregar_ticket("General", 5000)
sistema.agregar_ticket("VIP", 10000)

# Registrar ventas
total_venta_1 = sistema.registrar_venta("General", 10)
total_venta_2 = sistema.registrar_venta("VIP", 5)

# Mostrar ventas
ventas = sistema.obtener_ventas()
for venta in ventas:
    print(f"Tipo: {venta[0]}, Cantidad: {venta[1]}, Total Venta: ${venta[2]:,.2f}")
