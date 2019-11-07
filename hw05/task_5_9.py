'''9) Для каждого натурального числа в промежутке от m до n вывести все делители,
кроме единицы и самого числа. m и n вводятся с клавиатуры.
Пример:m =100, n = 105
'''

m = 100
n = 105



# while index < m:
#     if m % index == 0:
#         print(index)
#     index += 1

while m <= n:
    index = 2
    list_of_dividers = []
    while index < m:
        if m % index == 0:
            list_of_dividers.append(index)
        index += 1
    print(f'для {m} делители {list_of_dividers}')
    m += 1

