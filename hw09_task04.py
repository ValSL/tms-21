'''Создать универсальны декоратор, который меняет порядок аргументов в функции на противоположный.'''


def argument_reverse_decorator(func):
    def argument_rev(*args):
        func(*args[::-1])

    return argument_rev


@argument_reverse_decorator
def calc(a, b):
    res = a - b
    print(res)


@argument_reverse_decorator
def calc5(a, b, c, d, e):
    res = a - b - c - d - e
    print(res)


def main():
    calc(6, 2)
    calc5(20, 4, 3, 2, 1)


if __name__ == '__main__':
    main()
