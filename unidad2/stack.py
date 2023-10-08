# Estructura de datos - Pila
class Stack:
    '''
    Representa una pila con operaciones de apilar, desapilar y verificar si esta vacia
    '''

    def __init__(self) -> None:
        self.items = []  # La pila vacia se representa con una lista vacia

    def __str__(self) -> str:
        return " || ".join([str(i) for i in self.items])

    def push(self, value) -> None:
        # Push es agregar al final de la lista
        self.items.append(value)

    def pop(self):
        '''
        Devuelve el elemento tope y lo elimina de la pila.
        Si la pila esta vacia levanta una excepcion.
        '''
        if self.is_empty():
            print("La pila esta vacia")
            return
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("La pila esta vacia")
            return
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
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
