class Cafeteria:
    descuento_clientes_frecuentes = 0.1

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__menu = {}
        self.__pedidos = []

    def agregar_producto_menu(self, producto, precio):
        assert precio > 0, "El precio debe ser mayor a 0."
        if producto in self.__menu:
            return f"El producto '{producto}' ya está en el menú."
        self.__menu[producto] = precio
        self.__verificar_invariantes_menu()
        return f"Producto '{producto}' agregado al menú con precio ${precio}."

    def agregar_producto_pedido(self, producto, cantidad, frecuente=False):
        assert producto in self.__menu, f"El producto '{producto}' no está en el menú."
        assert cantidad > 0, "La cantidad debe ser mayor a 0."
        precio_unitario = self.__menu[producto]
        subtotal = precio_unitario * cantidad
        descuento = Cafeteria.calcular_precio_con_descuento(subtotal, Cafeteria.descuento_clientes_frecuentes) if frecuente else 0
        total = subtotal - descuento
        pedido = {
            "producto": producto,
            "cantidad": cantidad,
            "subtotal": subtotal,
            "descuento": descuento,
            "total": total
        }
        self.__pedidos.append(pedido)
        self.__verificar_invariantes_pedidos()
        return f"Producto '{producto}' agregado al pedido. Total: ${total:.0f}"

    def calcular_total_pedido(self):
        return sum(pedido["total"] for pedido in self.__pedidos)

    def mostrar_menu(self):
        if not self.__menu:
            return "El menú está vacío."
        return "\n".join(f"{producto}: ${precio}" for producto, precio in self.__menu.items())

    def mostrar_pedidos(self):
        if not self.__pedidos:
            return "No hay pedidos realizados."
        resultado = []
        for idx, pedido in enumerate(self.__pedidos, start=1):
            resultado.append(
                f"Pedido {idx}: {pedido['cantidad']}x {pedido['producto']} - "
                f"Subtotal: ${pedido['subtotal']:.0f}, "
                f"Descuento: ${pedido['descuento']:.0f}, "
                f"Total: ${pedido['total']:.0f}"
            )
        return "\n".join(resultado)

    @classmethod
    def actualizar_descuento(cls, nuevo_descuento):
        assert 0 <= nuevo_descuento <= 1, "El descuento debe estar entre 0 y 1."
        cls.descuento_clientes_frecuentes = nuevo_descuento
        return f"Tasa de descuento actualizada a {nuevo_descuento * 100:.0f}%."

    @staticmethod
    def calcular_precio_con_descuento(monto, descuento):
        assert monto >= 0, "El monto debe ser no negativo."
        assert 0 <= descuento <= 1, "El descuento debe estar entre 0 y 1."
        return monto * descuento

    def __verificar_invariantes_menu(self):
        assert all(precio > 0 for precio in self.__menu.values()), "Todos los precios en el menú deben ser mayores a 0."

    def __verificar_invariantes_pedidos(self):
        assert all(pedido["producto"] in self.__menu for pedido in self.__pedidos), "Todos los productos en pedidos deben estar en el menú."


cafeteria = Cafeteria("Cafetería La Taza")
print(cafeteria.agregar_producto_menu("café", 2000))
print(cafeteria.agregar_producto_menu("té", 1500))
print(cafeteria.agregar_producto_menu("pastel", 3000))
print("\nMenú actual:")
print(cafeteria.mostrar_menu())
print("\nAgregando pedidos:")
print(cafeteria.agregar_producto_pedido("café", 2, frecuente=True))
print(cafeteria.agregar_producto_pedido("pastel", 1))
print("\nPedidos realizados:")
print(cafeteria.mostrar_pedidos())
print(f"\nTotal del pedido actual: ${cafeteria.calcular_total_pedido():.0f}")
print("\nActualizando descuento:")
print(Cafeteria.actualizar_descuento(0.15))
print("\nAgregando otro pedido con el nuevo descuento:")
print(cafeteria.agregar_producto_pedido("té", 3, frecuente=True))
print("\nPedidos actualizados:")
print(cafeteria.mostrar_pedidos())
