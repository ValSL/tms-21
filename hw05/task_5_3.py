'''3) Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]
'''

list01 = list(range(200, 301))
index = 0

while index < len(list01):
    i1 = 1   # Счетчик для первгого цикла
    i2 = 1   # Счетчик для второго
    sum_all_dividers1 = 0   # Сумма всех делителей для первого числа
    sum_all_dividers2 = 0   # Сумма всех делителей для второго числа

    # Сумма всех делителей для одного числа
    while i1 < list01[index]:
        if list01[index] % i1 == 0:
            sum_all_dividers1 += i1
        i1 += 1

    for second_number in list01:
        if second_number == sum_all_dividers1:      # Ищу число которое равно сумме делителей первого
            while i2 < second_number:               # Сумма делителей второго
                if second_number % i2 == 0:
                    sum_all_dividers2 += i2
                i2 += 1

            if sum_all_dividers2 == list01[index]:      # Ищу число которое равно сумме делителей второго
                print(list01[index])
                print(second_number)
                print("_________")
    index += 1











