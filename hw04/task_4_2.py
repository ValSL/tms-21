''' Дан список целых чисел. Подсчитать сколько четных чисел в списке
'''

'''Способ 1'''
list01 = list(range(1, 13))
print(list01)
count = 0
count2 = 0

for i in list01:
    if i % 2 == 0:
        count += 1
print(count)


'''Способ 2'''
list01_len = len(list01)
i = 0

while i < list01_len:
    if list01[i] % 2 == 0:
        count2 += 1
    i += 1
print(count2)
