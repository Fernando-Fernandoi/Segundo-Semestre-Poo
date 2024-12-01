#Ejercicio 2

"""Diseñar un sistema de gestión de inventario utilizando una clase Inventario que gestione
múltiples objetos de tipo Producto. Este inventario debe ser un diccionario donde las claves
serán los códigos de los productos, y los valores serán instancias de cada Producto. Además
cada producto tendrá un historial de cambios en el stock utilizando una lista.
Clase Producto:
● Atributos:
○ El nombre del producto.
○ El precio por unidad.
○ La cantidad disponible del producto.
○ El código único (Código de Barra) del producto.
○ Una lista que registre el historial de cambios en el stock (incrementos o decrementos).
● Métodos de la clase Producto:
○ Crear método que actualice el stock del producto y añada el cambio al
historial de stock.
○ Implementar método que calcule el valor total de los productos disponibles
○ Crear método mágico para mostrar el estado actual del producto en formato texto.
Clase Inventario:
● Atributos:
○ Un diccionario de productos donde la clave es el código del producto y el
valor es una instancia de la clase Producto.
● Métodos de la clase Inventario:
○ Crear método que agregue un nuevo producto al inventario.
○ Implementar un método que actualice el stock de un producto en el inventario.
○ Crear método que muestre todos los productos del inventario y sus detalles.
○ Implementar un método que calcule el valor total de todos los productos en el inventario.
Se debe considerar en este ejercicio, la clase Inventario contiene productos (instancias de la clase
Producto), pero no hereda de Producto."""

class Producto:
    def __init__(self, nombre, precio, cantidad, codigo):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.codigo = codigo
        self.historial_stock = []
        self.historial_stock.append(f"Stock inicial: {cantidad} unidades")
    
    def actualizar_stock(self, cambio):
        self.cantidad += cambio
        if cambio > 0:
            self.historial_stock.append(f"Se agregaron {cambio} unidades. Total: {self.cantidad}")
        else:
            self.historial_stock.append(f"Se restaron {-cambio} unidades. Total: {self.cantidad}")
    
    def valor_total(self):
        return self.cantidad * self.precio
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Código: {self.codigo}"

class Inventario:
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, producto):
            self.productos[producto.codigo] = producto
            print(f"El producto {producto.nombre} fue agregado al inventario.")
    
    def actualizar_stock_producto(self, codigo, cambio):
        codigo in self.productos
        self.productos[codigo].actualizar_stock(cambio)
    
    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)
    
    def valor_total_inventario(self):
        total = sum(producto.valor_total() for producto in self.productos.values())
        return total

producto1 = Producto("Shampoo", 1500, 10, "001")
producto2 = Producto("Galleta", 800, 20, "002")
inventario = Inventario()
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.actualizar_stock_producto("001", 5)
inventario.actualizar_stock_producto("002", -3)
inventario.mostrar_productos()

print(f"Valor total del inventario: {inventario.valor_total_inventario()}")
print(f"Historial de stock del producto 001: {producto1.historial_stock}")
print(f"Historial de stock del producto 002: {producto2.historial_stock}")