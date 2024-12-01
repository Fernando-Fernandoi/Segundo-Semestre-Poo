#Ejercicio 5

"""5. Desarrollar un sistema de gestión de una biblioteca donde se pueda agregar y administrar
libros. Cada libro tiene un título, autor, año de publicación, y cantidad disponible del libro. La
biblioteca es responsable de gestionar los libros y permitir la búsqueda de libros por título.
Considerar crear la clase Biblioteca que debe manejar múltiples instancias de la clase Libro
utilizando un diccionario. Los libros se pueden agregar, buscar y actualizar """

class Libro:
    def __init__(self, titulo, autor, año, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.titulo} por {self.autor} ({self.año}), Cantidad disponible: {self.cantidad}"

class Biblioteca:
    def __init__(self):
        self.libros = {}

    def agregarlibro(self, libro):
        self.libros[libro.titulo] = libro
        print(f"El Libro '{libro.titulo}' ah sido agregado exitosamente.")

    def buscar_libro(self, titulo):
        if titulo in self.libros:
            return self.libros[titulo]
        else:
            print(f"El libro '{titulo}' no esta disponible.")
            return None

    def actualizar_cantidad(self, titulo, nueva_cantidad):
        libro = self.buscar_libro(titulo)
        libro.cantidad = nueva_cantidad
        print(f"La cantidad del libro '{titulo}' se ha actualizado a {nueva_cantidad}.")

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            for libro in self.libros.values():
                print(libro)

biblioteca = Biblioteca()

libro1 = Libro("Cronica de una muerte anunciada", "Gabriel García Márquez", 1981, 5)
libro2 = Libro("Harry Potter y la Píedra filosofal", "J.K. Rowling", 1997, 10)
libro3 = Libro("Papelucho", "Marcela Paz", 1947, 4)
libro4 = Libro("Cien Años de Soledad", "Gabriel Garcia Marquez", 1967, 7)

biblioteca.agregarlibro(libro1)
biblioteca.agregarlibro(libro2)
biblioteca.agregarlibro(libro3)
biblioteca.agregarlibro(libro4)

libro_buscado = biblioteca.buscar_libro("Cronica de una muerte anunciada")
if libro_buscado:
    print("Libro encontrado:")
    print(libro_buscado)

biblioteca.actualizar_cantidad("Harry Potter y la Píedra filosofal", 9)

print("Libros en la biblioteca:")
biblioteca.mostrar_libros()