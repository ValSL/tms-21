'''Составить список чисел Фибоначчи содержащий 15 элементов.
'''
import random


list01 = [1, 1]
i = 2

while i < 15:
    list01.insert(i, list01[i-1] + list01[i-2])
    i += 1
print(list01)

'''Способ 2'''
'''Не придумал как сделать с циклом for'''

list02 = [1, 1]
list03 = []
count = 0

for i in list02:
    if i == 1:
        continue
    if count >15:
        break
    list02.insert(i, list01[i-1] + list01[i-2])
    count += 1

print(list02)
