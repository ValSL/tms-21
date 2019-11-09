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

'''Найти минимальный минимальный матрицы.'''

min = matrix[0][0]
matrix_len = len(matrix)

for index in matrix:
    for elem in index:
        if elem < min:
            min = elem

print(f"Минимальный элемент {min}")
print("_______________________")

'''Найти сумму всех элементов матрицы.'''

matrix_sum = 0

for index in matrix:
    for elem in index:
        matrix_sum += elem

print(f"Сумма всех элементов {matrix_sum}")
print("__________________________")

'''Найти индекс ряда с максимальной суммой элементов.'''

line_index = -1
max_line_sum = 0
max_line_index = 0

for index in matrix:
    line_sum = 0
    line_index +=1
    for elem in index:
        line_sum += elem
    if line_sum > max_line_sum:
        max_line_sum = line_sum
        max_line_index = line_index

print(f'Индекс ряда с максимальной суммой элементов {max_line_index}')
print("_________________________________________")


