'''Создать lambda функцию, которая принимает на вход неопределенное количество именных аргументов
и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}
'''


def main():
    func = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}
    print(func(a=2, b=3, ddd=4))


if __name__ == '__main__':
    main()
