'''7) Дана целочисленная квадратная матрица. Найти в каждой строке наи-
больший элемент и поменять его местами с элементом главной диагонали.
[02-4.2-ML22]
'''
list01 = [[1, 2, 3, 1], [4, 5, 6, 8], [7, 8, 9, 6], [6, 3, 2, 2]]

for i in list01:
    print(i)

line_index = 0

list01_len = len(list01)

while line_index < list01_len:
    column_index = 0
    max = 0
    max_index = 0
    while column_index < len(list01[line_index]):
        if list01[line_index][column_index] > max:  # Ищу максимальное число и его индекс в строке
            max = list01[line_index][column_index]
            max_index += 1
        column_index += 1

    temp = list01[line_index][line_index]  # Меняю местами max и элемент диагонали
    list01[line_index][line_index] = max
    list01[line_index][max_index - 1] = temp
    line_index += 1

print('_______________')

for i in list01:
    print(i)
