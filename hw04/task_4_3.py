'''Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
 Чтобы получить список ключей - использовать метод .keys()
'''

dict01 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

list01_keys = dict01.keys()

for i in list(list01_keys):
    number = len(i)
    number_str = str(number)
    dict01[i + number_str] = dict01.pop(i)

print(dict01)

'''Способ 2'''
dict02 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

list02_keys = list(dict02.keys())
index = 0

while index < len(dict02):
    i = list02_keys[index]
    number_2 = 0
    number_2 = len(list02_keys[index])
    number_2_str = str(number_2)
    dict02[i+number_2_str] = dict02.pop(i)
    index += 1
print(dict02)






