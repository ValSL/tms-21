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


