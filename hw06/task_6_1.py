'''Создать матрицу случайных чисел от a до b, размерность матрицы n*m'''
import random

n = 3
m = 3
matrix = []

for row in range(n):
    mass_line = []
    for line in range(m):
        mass_line.append(random.randint(0, 9))
        print(mass_line[line], end = "  ")
    matrix.append(mass_line)
    print("\n")
print("_______________")


'''Найти максимальный элемент матрицы.'''
max = matrix[0][0]
matrix_len = len(matrix)

for index in matrix:
    for elem in index:
        if elem > max:
            max = elem

print(f'Максимальный элемент {max}')
print("_______________________")

