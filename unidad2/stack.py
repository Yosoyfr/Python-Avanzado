class Stack:
    """ 
    Representa una pila con operaciones de apilar, desapilar y verificar si está vacía. 
    """

    def __init__(self):
        self.items = []  # La pila vacía se representa con una lista vacía

    def push(self, value):
        # Push es agregar al final de la lista.
        self.items.append(value)

    def pop(self):
        """ 
        Devuelve el elemento tope y lo elimina de la pila.
        Si la pila está vacía levanta una excepción. 
        """
        # Verificamos que la pila no este vacia
        if self.is_empty():
            print('La pila esta vacia')
            return
        return self.items.pop()

    def peek(self):
        # Verificamos que la pila no este vacia
        if self.is_empty():
            print('La pila esta vacia')
            return
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0


pila = Stack()

pila.push(1)
pila.push(2)
pila.push(3)


print(pila.items)
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())
print(pila.peek())
