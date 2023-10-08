class PriorityQueue:

    def __init__(self) -> None:
        self.queue = []

    def __str__(self) -> str:
        return ' || '.join([str(i) for i in self.queue])

    def size(self) -> int:
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        try:
            max = 0  # Acarrea el indice del dato con mayor prioridad
            for i in range(self.size()):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()


'''
queue = PriorityQueue()

queue.enqueue(10)
queue.enqueue(5)
queue.enqueue(15)
queue.enqueue(100)

print(queue)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
'''


class Boleto:

    def __init__(self, nombre, precio, localidad) -> None:
        # Localidad hace referencia a el lugar del boleto [GRADAS, GENERAL, MESAS, VIP]
        self.nombre = nombre
        self.precio = precio  # [100, 300, 500, 1000]
        self.localidad = localidad

    def __str__(self) -> str:
        return str(self.nombre) + " - " + str(self.localidad)


LOCALIDAD = {
    "GRADAS": 1, "GENERAL": 2, "MESAS": 3, "VIP": 4
}


class ColaConcierto:
    def __init__(self) -> None:
        self.queue = []

    def __str__(self) -> str:
        return ' || '.join([str(i) for i in self.queue])

    def size(self) -> int:
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        try:
            max = 0  # Acarrea el indice del dato con mayor prioridad
            for i in range(self.size()):
                if LOCALIDAD[self.queue[i].localidad] > LOCALIDAD[self.queue[max].localidad]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except:
            print()
            exit()


concierto = ColaConcierto()

boleto1 = Boleto("Francisco Suarez", 300, "GENERAL")
boleto2 = Boleto("Santiago Vasquez", 1000, "VIP")
boleto3 = Boleto("Luis Suarez", 500, "MESAS")
boleto4 = Boleto("Francisco Lopez", 100, "GRADAS")
boleto5 = Boleto("Santiago Ramirez", 1000, "VIP")

# print("Boleto:", boleto1)

concierto.enqueue(boleto1)
concierto.enqueue(boleto2)
concierto.enqueue(boleto3)
concierto.enqueue(boleto4)
concierto.enqueue(boleto5)

print("Cola:", concierto)

print('Como fueron ingresando al concierto:')
print(concierto.dequeue())
print(concierto.dequeue())
print(concierto.dequeue())
print(concierto.dequeue())
print(concierto.dequeue())
