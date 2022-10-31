from collections import deque

queue = deque()

queue.append(1)  # Insertar 1 en la cola
queue.append(2)  # Insertar 2 en la cola
queue.append(3)  # Insertar 3 en la cola
queue.append(4)  # Insertar 4 en la cola

# print('The front element is', queue[0])     # 1

# Insercion de datos al final
queue.appendleft(5)
# print('The front element is', queue[0])     # 5


# Eliminar datos de la cola al final
# print('The last element is', queue[-1])
# queue.pop()
# print('The last element is', queue[-1])


# Eliminar datos de la cola al frente
print('The last element is', queue[0])
queue.popleft()
print('The last element is', queue[0])
