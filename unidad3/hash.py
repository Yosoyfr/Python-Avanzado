# Tabla Hash
import hashlib


class HashTable:
    def __init__(self) -> None:
        self.table = [[] for _ in range(127)]

    # Funcion Hash
    def hash_func(self, value):
        key = 0
        for i in range(0, len(value)):
            key += ord(value[i])
        return key % 127

    def insert(self, value):  # Metodo para registrar elementos
        hash = self.hash_func(value)
        self.table[hash].append(value)

    def search(self, value):  # Metodo para buscar elementos
        hash = self.hash_func(value)
        if len(self.table[hash]) > 0:
            if value in self.table[hash]:
                return hex(id(value))
        return None

    def remove(self, value):  # Metodo para eleminar elementos
        hash = self.hash_func(value)
        if len(self.table[hash]) > 0:
            for i in range(0, len(self.table[hash])):
                del self.table[hash][i]
                print("Elemento con valor:", value, " ha sido eliminado")
                return
        print("No hay elementos con el valor:", value)


'''
table = HashTable()
table.insert("Francisco")
table.insert("Santiago")
table.insert("Ana")

table.remove("Francisco")

result = table.search("Francisco")
print(result)
'''


class Contacto():
    def __init__(self, nombre, telefono, _direccion="", _correo="") -> None:
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = _direccion
        self.correo = _correo

    def __str__(self) -> str:
        return str({"nombre": self.nombre, "telefono": self.telefono, "direccion": self.direccion, "correo": self.correo})


ct1 = Contacto("Francisco Suarez", 11111111, "Guatemala")
ct2 = Contacto("Santiago Vasquez", 22222222, "Guatemala", "santiago@gmail.com")
ct3 = Contacto("Luis Lopez", 33333333, "Mexico")
ct4 = Contacto("Ana Soto", 44444444, "El Salvador")
ct5 = Contacto("Jose Jimenez", 55555555, "Puerto Rico")
ct6 = Contacto("Francisco Suarez", 66666666, "Honduras")


class ListaContactos():
    def __init__(self, _capacity=127) -> None:
        self.capacity = _capacity
        self.table = [[] for _ in range(_capacity)]

    def hash_func(self, value) -> int:
        aux = hashlib.md5(value.encode()).hexdigest()
        key = 0
        for i in range(0, len(aux)):
            key += ord(aux[i])
        return key % self.capacity

    def insert(self, contact):
        hash = self.hash_func(contact.nombre)
        self.table[hash].append(contact)

    def search(self, nombre):
        hash = self.hash_func(nombre)
        if len(self.table[hash]) > 0:
            _lista = []
            for contact in self.table[hash]:
                if nombre == contact.nombre:
                    _lista.append(str(contact))
            return _lista
        return None


lista_contactos = ListaContactos()
lista_contactos.insert(ct1)
lista_contactos.insert(ct2)
lista_contactos.insert(ct3)
lista_contactos.insert(ct4)
lista_contactos.insert(ct5)
lista_contactos.insert(ct6)

busqueda = lista_contactos.search("Francisco Suarez")
print(str(busqueda))
