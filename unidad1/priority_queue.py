class PriorityQueue:

    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def insert(self, value):
        self.queue.append(value)

    def delete(self):
        try:
            max = 0
            for i in range(self.size()):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()


queue = PriorityQueue()
'''
queue.insert(10)
queue.insert(5)
queue.insert(20)
queue.insert(14)

print(queue)

print(queue.delete())
print(queue.delete())
print(queue.delete())
print(queue.delete())
'''


class Boleto:

    def __init__(self, location, precio, nombre) -> None:
        # Location hace referencia a el lugar del boleto [GRADAS, GENERAL, MESAS, VIP]
        self.location = location
        self.precio = precio
        self.nombre = nombre

    def __str__(self):
        return str(self.nombre)


class ColaConcierto:

    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def insert(self, value):
        self.queue.append(value)

    def delete(self):
        try:
            max = 0
            for i in range(self.size()):
                if self.queue[i].location > self.queue[max].location:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()


concierto = ColaConcierto()

boleto1 = Boleto(1, 300, 'General')
boleto2 = Boleto(1, 300, 'General')
boleto3 = Boleto(0, 100, 'Gradas')
boleto4 = Boleto(3, 1000, 'Vip')
boleto5 = Boleto(2, 500, 'Mesas')

concierto.insert(boleto2)
concierto.insert(boleto5)
concierto.insert(boleto1)
concierto.insert(boleto4)
concierto.insert(boleto3)

print('Cola:', concierto)

print('Como fueron ingresando al concierto:')
print(concierto.delete())
print(concierto.delete())
print(concierto.delete())
print(concierto.delete())
print(concierto.delete())
