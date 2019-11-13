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


'''Найти индекс колонки с максимальной суммой элементов.'''

max_column_sum = matrix[0][0]
max_column_index = -1
row = 0

while row < len(matrix):
    column_sum = 0
    column = 0
    while column < len(matrix):
        column_sum += matrix[column][row]
        column += 1
    if max_column_sum < column_sum:
        max_column_sum = column_sum
        max_column_index += 1
    row += 1

print(f"Индекс колонки с максимальной суммой элементов {max_column_index}")
print("_____________________________________________________________")

'''Найти индекс ряда с минимальной суммой элементов.'''

line_index_count = -1
min_line_sum = 0
min_line_index = 0

for line in matrix:
    for column in line:
        min_line_sum += column
    break

for index in matrix:
    line_sum = 0
    for elem in index:
        line_sum += elem
    line_index_count += 1
    if line_sum < min_line_sum:
        min_line_sum = line_sum
        min_line_index = line_index_count

print(f'индекс ряда с минимальной суммой элементов {min_line_index}')
print("_______________________________________________")

'''Найти индекс колонки с минимальной суммой элементов.'''


min_row = 0
column_summ = 0
while min_row < len(matrix):
    column = 0
    while column < len(matrix):
        column_summ += matrix[column][min_row]
        column += 1
    break

min_column_sum = column_summ

min_column_index = 0
min_column_count = -1
while min_row < len(matrix):
    column_sum = 0
    column = 0
    while column < len(matrix):
        column_sum += matrix[column][min_row]
        column += 1
    min_column_count += 1

    if min_column_sum > column_sum:
        min_column_sum = column_sum
        min_column_index = min_column_count

    min_row += 1

print(f'индекс колонки с минимальной суммой элементов {min_column_index}')
print("_________________________________________________________")

'''Обнулить все элементы выше главной диагонали.'''

index_in_line = 0


while index_in_line < len(matrix):
    index_in_col = 0
    pos_of_main_diag = 0
    position_index = 0

    while index_in_col < len(matrix):
        pos_of_main_diag = index_in_line

        if index_in_line == index_in_col:
            position_index += 1
            index_in_col += 1
            continue

        if position_index > pos_of_main_diag:
            matrix[index_in_line][index_in_col] = 0

        position_index += 1
        index_in_col += 1
    index_in_line += 1

for i in matrix:
    print(i)

print("_________________________")

'''Обнулить все элементы ниже главной диагонали.'''

index_in_line = 0


while index_in_line < len(matrix):
    index_in_col = 0
    pos_of_main_diag = 0
    position_index = 0

    while index_in_col < len(matrix):
        pos_of_main_diag = index_in_line

        if index_in_line == index_in_col:
            position_index += 1
            index_in_col += 1
            continue

        if position_index < pos_of_main_diag:
            matrix[index_in_line][index_in_col] = 0

        position_index += 1
        index_in_col += 1
    index_in_line += 1

for i in matrix:
    print(i)
print("_______________________________")

'''Создать две новые матрицы matrix_a, matrix_b случайных чисел размерностью n*m. '''
print("Создать две новые матрицы matrix_a, matrix_b случайных чисел размерностью n*m. ")
n2 = 3
m2 = 3
matrix_a = []
matrix_b = []

for col in range(n2):
    matrix_line = []
    for line in range(m2):
        matrix_line.append(random.randint(0, 9))
    matrix_a.append(matrix_line)

for col in range(n2):
    matrix_line = []
    for line in range(m2):
        matrix_line.append(random.randint(0, 9))
    matrix_b.append(matrix_line)
for i in matrix_a:
    print(i)

print("")

for i in matrix_b:
    print(i)

'''Создать матрицу равную сумме matrix_a и matrix_b.'''
print("")
matrix_a_plus_b = []

line = 0

while line < len(matrix_a):
    matrix_ab_line = []
    col = 0
    while col < len(matrix_a):
        elem_sum = matrix_a[line][col] + matrix_b[line][col]
        matrix_ab_line.append(elem_sum)
        col += 1
    matrix_a_plus_b.append(matrix_ab_line)
    line += 1

print("Матрица равная сумме matrix_a и matrix_b.")
for i in matrix_a_plus_b:
    print(i)
print("__________________________________")

'''Создать матрицу равную разности matrix_a и matrix_b.'''

matrix_a_minus_b = []
line = 0

while line < len(matrix_a):
    matrix_ab_line = []
    col = 0
    while col < len(matrix_a):
        elem_diff = matrix_a[line][col] - matrix_b[line][col]
        matrix_ab_line.append(elem_diff)
        col += 1
    matrix_a_minus_b.append(matrix_ab_line)
    line += 1

print("Матрица равная разности matrix_a и matrix_b.")
for i in matrix_a_minus_b:
    print(i)

'''Создать новую матрицу равную matrix_a умноженной на g. g вводится с клавиатура'''

g = int(input("Ввести число: "))

matrix_a_multiply_g = []

line = 0

while line < len(matrix_a):
    matrix_ab_line = []
    col = 0
    while col < len(matrix_a):
        elem_mult = matrix_a[line][col] * g
        matrix_ab_line.append(elem_mult)
        col += 1
    matrix_a_multiply_g.append(matrix_ab_line)
    line += 1

print("Матрица равная matrix_a умноженная на g")
for i in matrix_a_multiply_g:
    print(i)
