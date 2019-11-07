'''5) В массиве целых чисел с количеством элементов 19 определить максимальное число
и заменить им все четные по значению элементы. [02-4.1-BL19]
'''
import random
list01 = []
i = 0
max = 0 # max должно быть первый элемент массива, тк. могут быть и отрицательные числа
while i < 19:
    list01.append(random.randint(1, 21))
    i += 1
print(list01)

for i in list01:
    if i > max:
        max = i
print(max)

i2 = 0
while i2 < len(list01):
    if list01[i2] % 2 == 0:
        list01[i2] = max
    i2 += 1

print(list01)
