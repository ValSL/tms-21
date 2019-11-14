'''Создать функцию, принимающая на вход неопределенное количество аргументом и возвращающая сумму args[i] * i
Пример:  args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10
'''

def my_func(*args):
    index = 0
    res = 0
    while index < len(args):
        res = res + args[index] * index
        index += 1
    return res


print(my_func(4, 3, 2, 1))
