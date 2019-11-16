'''Создать функцию, которая принимает на вход неопределенное количество именных аргументов
и выводит на экран те из них, длина ключа которых четна.
'''

def my_func(**kwargs):
    for key, value in kwargs.items():
        if len(key) %2 == 0:
            print(key)


my_func(a=5, ab=3, abc=1, abcd=0, abcde=2, abcdef=9)
