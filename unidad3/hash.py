class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(127)]

    # Función hash
    def hash_func(self, value):
        key = 0
        for i in range(0, len(value)):
            key += ord(value[i])
        return key % 127

    def insert(self, value):  # Metodo para ingresar elementos
        hash = self.hash_func(value)
        self.table[hash].append(value)

    def search(self, value):  # Metodo para buscar elementos
        hash = self.hash_func(value)
        if len(self.table[hash]):
            if value in self.table[hash]:
                return hex(id(value))
        return None

    def remove(self, value):  # Metodo para eleminar elementos
        hash = self.hash_func(value)
        if len(self.table[hash]):
            for i in range(0, len(self.table[hash])):
                if self.table[hash][i] == value:
                    del self.table[hash][i]
                    print("Elemento con valor", value, "eliminado")
                    return
        print("No hay elementos con ese valor", value)


H = HashTable()
H.insert("A")
H.insert("A")
H.insert("B")
H.insert("C")

print(H.search("A"))

H.remove("A")
H.remove("A")
H.remove("A")
H.remove("B")
H.remove("C")
H.remove("D")
