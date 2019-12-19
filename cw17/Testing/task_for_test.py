# Дан массив целых чисел A. Найти суммы положительных
# и отрицательных элементов массива, используя функцию
# определения суммы. [02-5.1-BL21]


def calc_sum(numbers):
    pos_sum = 0
    neg_sum = 0
    for number in numbers:
        if number > 0:
            pos_sum += number
        elif number < 0:
            neg_sum += number
    return pos_sum, neg_sum

