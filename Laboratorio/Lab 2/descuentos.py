"""1. Encapsulación de Datos del Cliente
A. ¿Qué datos del cliente crees que deben encapsularse en una clase Cliente? Considera atributos como el tipo de cliente (estudiante, académico, otro) y el precio de la compra. 
¿Cuál de estos atributos debería ser privado y cuál público? ¿Por qué?

R: Los datos del cliente que deberian encapsularse en una clase Cliente son el tipo de cliente y el precio de la compra. Por que se puede encapsular la información y protegerla de modificaciones accidentales.
El atributo que deberia ser publico deberia ser el precio de la compra? Esto es porque es el dato más importante y crucial que un cliente debe poder ver y modificar. 
Y el privado debe ser el tipo de cliente para que la información no sea modificable de manera accidental.

2. Diccionario de Descuentos
A. ¿Cómo organizarías los descuentos disponibles para cada tipo de cliente en el sistema? ¿Crees que un diccionario privado podría ser útil para almacenar los descuentos para cada tipo de cliente? ¿o se necesita otro tipo de estructura de datos?
B. ¿Por qué sería útil encapsular la estructura de datos anterior de descuentos en lugar de exponerlo directamente?

R: Yo organizaria los descuentos disponibles para cada tipo de cliente en un diccionario privado. Porque esto permitiría almacenar los descuentos para cada tipo de cliente de manera fácil. 
Esto facilita la reutilización de la información y aumenta la claridad del sistema.

Variables de Clase
1. Definición de Descuentos
A. ¿Cómo definirías los descuentos para cada tipo de cliente en el sistema? Considera que el descuento para los estudiantes es del 20% y para los académicos del 10%.
B. ¿Crees que estos descuentos deberían ser variables de clase o variables de instancia? Justifica tu respuesta en términos de reutilización y claridad del sistema.

R: Los descuentos los definiria en variables de clase. Los definiciones en variables de clase para que sean compartidas por todas las instancias de la clase, 
lo que puede ser útil para evitar la duplicación de código y facilitar la reutilización de la lógica de descuentos.

Accesores y Mutadores
1. Métodos para Modificar el Precio de Compra
A. ¿Cómo permitirías la modificación del precio de la compra de un cliente sin que se afecte la lógica de descuentos? ¿Crees que sería útil usar un setter para ajustar el precio antes de aplicar el descuento?
B. ¿Qué tipo de acceso debería tener el descuento del cliente? ¿Cómo un getter podría facilitar la obtención del precio final sin exponer el cálculo interno?

R: Yo permitiria usar un setter para ajustar el precio antes de aplicar el descuento. Esto puede ayudar a evitar que el precio sea modificado de manera accidental y facilitar la reutilización de la lógica de descuentos.
El tipo de acceso que deberia tener el descuento del cliente sería privado para que no se pueda modificar de manera accidental. El getter se podria utilizar para obtener el valor de un atributo privado sin afectar la obtencion del precio final. 

Métodos Estáticos
1. Cálculo del Precio Final
A. Imagina que deseas implementar un método que calcule el precio final después de aplicar el descuento correspondiente. ¿Por qué sería conveniente implementar este método como un método estático?


B. ¿Qué ventajas tiene usar un método estático en este caso, en comparación con un método de instancia?R: Seria conveniente implementar este método como un método estático para que pueda ser llamado sin necesidad de crear una instancia de la clase. 
Las ventajas de usar un método estático en este caso son que puede ser llamado sin necesidad de crear una instancia de la clase, lo que puede ser útil para asegurar el código y evitar duplicaciones.2. Implementación del Descuento


A. Si decides crear un método estático ¿qué parámetros debería recibir este método y qué valor debería devolver? ¿Por qué?
R: Los parametros del método estático podrían ser el precio y el tipo de cliente. El valor debería devolver el precio final después de aplicar el descuento. 

Porque este método puede ser reutilizado para calcular el precio final para cualquier tipo de cliente.

Asertos e Invariantes
1. Verificación del Precio
A. ¿Qué asertos consideras que serían útiles para asegurar que el precio de una compra no sea negativo? ¿Cómo evitarías que se realice una compra con un valor incorrecto?
2. Control de Descuentos y Validación del Tipo de Cliente
A. ¿Qué invariante podrías establecer para asegurarte de que el descuento sólo se aplica si el tipo de cliente es válido (es decir, estudiante o académico)?
B. ¿Cómo usarías asertos para verificar que el tipo de cliente ingresado esté dentro de los tipos válidos antes de aplicar el descuento

R: Los asertos que considero útiles para asegurar que el precio de una compra no sea negativo son que el método set_precio() verifica que el precio sea mayor o igual a cero.
Yo evito que se realice una compra con un valor incorrecto estableciendo un aserto que el tipo de cliente ingresado esté dentro de los tipos válidos.
De ahi ya no se :( sorry
"""
#Se define la clase Cliente con los atributos y métodos requeridos.
class Cliente:
    _descuentos = {
        "estudiante": 0.20,
        "academico": 0.10,
        "otro": 0.00
    }

    def __init__(self, tipo):
        if tipo not in self._descuentos:
            raise ValueError("Tipo de cliente no válido")
        self._precio = 0.0
        self._tipo = tipo
        self._validar_precio()
    
    def get_precio(self):
        return self._precio
    
    def set_precio(self, valor):
        self._precio = valor
        self._validar_precio()
    
    def aplicar_descuento(self):
        descuento = self._descuentos.get(self._tipo, 0.0)
        precio_final = self._precio * (1 - descuento)
        return precio_final
    
    @staticmethod
    def calcular_precio_final(precio, tipo):
        if tipo not in Cliente._descuentos:
            raise ValueError("Tipo de cliente no válido")
        descuento = Cliente._descuentos.get(tipo, 0.0)
        precio_final = precio * (1 - descuento)
        return precio_final
    
    def _validar_precio(self):
        if self._precio < 0:
            raise ValueError("Precio de compra no puede ser negativo")
    
    def get_tipo(self):
        return self._tipo
    
    def set_tipo(self, tipo):
        if tipo not in self._descuentos:
            raise ValueError("Tipo de cliente no válido")
        self._tipo = tipo
        self._validar_precio()
    
    def __str__(self):
        return f"Cliente: {self._tipo}, Precio: {self._precio}"
    
    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self._tipo == other._tipo and self._precio == other._precio
        return False
    
    def __hash__(self):
        return hash((self._tipo, self._precio))