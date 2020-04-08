# zadanie 2
import random

matrix = [random.sample(range(0, 10), 4), random.sample(range(0, 10), 4), random.sample(range(0, 10), 4), random.sample(range(0, 10), 4)]
print(matrix)
lista = [matrix[index][index] for index in [0, 1, 2, 3]]
print(lista)