# Metodos necesarios para crea una cola

# enqueue: Insercion de datos por la parte trasera de la cola
# dequeue: Elimina/Devuelve el dato al frente de la cola
# peek: Devuelve el elemento al frente de la cola (sin eliminarlo)
# is_empty: Devuelve si la cola esta vacia (True/False)
# size: Devuelve el numero total de elemento en la cola
# is_full: Devuelve si la cola esta llena (True/False) (opcional)


# Argumentos
# size

class Queue:

    def __init__(self, size=1000):
        self.q = [None] * size  # Lista # para almacenar elementos de queue
        self.capacity = size    # capacidad máxima de la queue
        self.front = 0          # front apunta al elemento frontal en la queue
        self.rear = -1          # La parte trasera de # apunta al último elemento de la queue
        self.count = 0          # tamaño actual de la queue

    # enqueue: Insercion de datos por la parte trasera de la cola
    def enqueue(self, value):
        # Verificamos que la cola no este llena
        if self.is_full():
            print('La cola esta llena')
            return
        print('Insertando elemento...', value)
        self.rear = (self.rear+1) % self.capacity
        self.q[self.rear] = value
        self.count += 1

    # dequeue: Elimina el dato al frente de la cola
    def dequeue(self):
        # Verificamos que la cola no este vacia
        if self.is_empty():
            print('La cola esta vacia')
            return
        aux = self.q[self.front]
        print('Removiendo el elemento...', aux)
        self.front = (self.front+1) % self.capacity
        self.count -= 1
        return aux

    def peek(self):
        # Verificamos que la cola no este vacia
        if self.is_empty():
            print('La cola esta vacia')
            return
        return self.q[self.front]

    def size(self):
        return self.count

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity


# Crear una cola
'''
cola = Queue(5)

cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
cola.enqueue(4)
cola.enqueue(5)
print('El tamaño de la cola es...', cola.size())

elemento = cola.dequeue()
elemento = cola.dequeue()
cola.enqueue(10)
elemento = cola.dequeue()
elemento = cola.dequeue()
elemento = cola.dequeue()
elemento = cola.dequeue()

print(cola.q)

print('El tamaño de la cola es...', cola.size())
'''
