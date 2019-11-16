'''Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент mean_type.
В зависимости от mean_type вернуть среднеарифметическое либо среднегеометрическое.
Написать программу в виде трех функций.
'''

def arithmetic_mean(*args):
    num_sum = 0
    number_count = 0
    for number in args:
        num_sum += number
        number_count += 1
    avg = num_sum / number_count
    return avg


def geometric_mean(*args):
    num_mult = 1
    number_count = 0
    for number in args:
        num_mult *= number
        number_count += 1
    avg = num_mult**(1/number_count)
    return avg


def my_func(*args, mean_type):
    if mean_type == "arithmetic":
        res = arithmetic_mean(*args)
        return res
    elif mean_type == "geometric":
        res = geometric_mean(*args)
        return res



a = my_func(5, 3, 12, mean_type="geometric")
print(a)

