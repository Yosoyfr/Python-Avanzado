# Metodos necesarios para crear una cola

# enqueue: Insercion de datos por la parte trasera de la cola
# dequeue: Elimina/Devuelve el dato al frente de la cola
# peek: Devuelve el elemento al frente de la cola (sin eliminarlo)
# is_empty: Devuelve si la cola esta vacia (True/False)
# size: Devuelve el numero total de elemento en la cola
# is_full: Devuelve si la cola esta llena (True/False) (opcional)


class Queue:

    def __init__(self, size=1000) -> None:
        self.q = [None]*size  # Lista para almacenar elementos de la cola
        self.capacity = size  # Capacidad maxima de la cola
        self.front = 0  # Front apunta al elemento frontal en la cola (HEAD)
        # La parte trasera apunta al ultimo elemnto de la cola (REAR)
        self.rear = -1
        self.count = 0  # Tamaño actual de la cola

    # enqueue: Insercion de datos por la parte trasera de la cola
    def enqueue(self, value) -> None:
        # Verificamos que la cola no este llena
        if self.is_full():
            print("La cola esta llena")
            return
        print("Insertando elemento...", value)
        self.rear = (self.rear+1) % self.capacity
        self.q[self.rear] = value
        self.count += 1

    # dequeue: Elimina el dato al frente de la cola
    def dequeue(self) -> None:
        # Verificamos que la cola no este vacia
        if self.is_empty():
            print("La cola esta vacia")
            return
        aux = self.q[self.front]
        print("Removiendo el elemento...", aux)
        self.front = (self.front+1) % self.capacity
        self.count -= 1
        return aux

    def peek(self):
        # Verificamos que la cola no este vacia
        if self.is_empty():
            print("La cola esta vacia")
            return
        return self.q[self.front]

    def is_empty(self) -> bool:
        return self.count == 0  # True | False

    def is_full(self) -> bool:
        return self.count == self.capacity  # True | False

    def size(self) -> int:
        return self.count


# Crear una cola
cola = Queue(10)

cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
cola.enqueue(4)

cola.dequeue()
cola.dequeue()

cola.enqueue(5)

print("El tamaño de la cola es...", cola.size())

print("Front:", cola.front)
print("Rear:", cola.rear)
