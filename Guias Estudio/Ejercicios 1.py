class Contacto:
    def __init__(self, nombre, telefono, email):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email

    def editar(self, nombre=None, telefono=None, email=None):
        if nombre: self.__nombre = nombre
        if telefono: self.__telefono = telefono
        if email: self.__email = email

    def __str__(self):
        return f"Nombre: {self.__nombre}, Teléfono: {self.__telefono}, Email: {self.__email}"


class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, contacto):
        self.contactos.append(contacto)

    def listar_contactos(self):
        return "\n".join(str(contacto) for contacto in self.contactos)

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.__str__().lower().startswith(nombre.lower()):
                return contacto
        return "Contacto no encontrado."

    def editar_contacto(self, nombre, telefono=None, email=None):
        contacto = self.buscar_contacto(nombre)
        if isinstance(contacto, Contacto):
            contacto.editar(telefono=telefono, email=email)
            return "Contacto actualizado."
        return "Contacto no encontrado."
