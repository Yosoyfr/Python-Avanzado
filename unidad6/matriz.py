# Matrices => Una lista de listas

import numpy as np

'''
    Las filas son interpretadas como las listas interiores
    Las columnas son interpretadas como los elementos de cada una de las listas
    Nomenclatura para definir la dimension es: (Filas)x(Columnas)
'''
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]  # => Filas: 3 - Columnas: 3 -> Matriz: 3x3


# Proceso de dibujo de una matriz

def dibujar_matriz(matriz):
    dibujo = ''
    _fila = 0

    for fila in matriz:
        dibujo += '['
        for columna in fila:
            dibujo += f'{str(columna)},'
        dibujo = dibujo[:len(dibujo) - 1]
        dibujo += f'] => {_fila}\n'
        _fila += 1

    return dibujo


# print(dibujar_matriz(matriz))


# Acceder a los datos de una matriz
indice_fila = 2
indice_columna = 0
valor_encontrado = matriz[indice_fila][indice_columna]
# print(valor_encontrado)

# Modificar a los datos de una matriz
indice_fila = 2
indice_columna = 0
matriz[indice_fila][indice_columna] = 100
# print(dibujar_matriz(matriz))


# Numpy -> Matrices
matriz = [[1, 2, 3, 'a'],
          [4, 5, 6, 'b'],
          [7, 8, 9, 'c']]  # => Filas: 3 - Columnas: 4 -> Matriz: 3x4

np_matriz = np.array(matriz)
# print(np_matriz)

np_eye = np.eye(5, 5, dtype=int)
# print(np_eye)

np_identity = np.identity(10)
# print(np_identity)

np_ones = np.ones((10, 10))
# print(np_ones)

np_zeros = np.zeros((10, 10))
# print(np_zeros)

# Acceder a elementos
print(np_matriz[1][3])

# Modificar a elementos
np_matriz[1][3] = 'z'
# print(np_matriz)


# Suma de matrices
matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]  # => Filas: 3 - Columnas: 3 -> Matriz: 3x3
matriz2 = [[10, 20, 30],
           [40, 50, 60],
           [70, 80, 90]]  # => Filas: 3 - Columnas: 3 -> Matriz: 3x32

np_matriz1 = np.array(matriz1)
np_matriz2 = np.array(matriz2)

np_result = np_matriz1 + np_matriz2
print(np_result)
