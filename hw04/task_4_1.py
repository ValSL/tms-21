'''Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2
'''

list01 = [1, 2, 3, 4, 5]
list02 = []# Первый способ
list03 = []# Второй способ

for i in list01:
    list02.append(i * -2)

print(list02)

''' Способ 2 '''

list01_len = len(list01)
i = 0

while i < list01_len:
    list03.append(list01[i] * -2)
    i += 1
print(list03)



