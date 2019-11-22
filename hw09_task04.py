'''Создать универсальны декоратор, который меняет порядок аргументов в функции на противоположный.'''


def argument_reverse_decorator(func):
    def argument_rev(a, b):
        func(b, a)
    return argument_rev


@argument_reverse_decorator
def calc(a, b):
    res = a - b
    print(res)


def main():
    calc(6, 2)


if __name__ == '__main__':
    main()
