'''Создать декоратор для функции, которая принимает список чисел.
 Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка.
'''


def decorator_without_even(func):
    def delete_all_even(any_list):
        for index, value in enumerate(any_list):
            if value % 2 == 0:
                any_list.pop(index)
        func(any_list)
    return delete_all_even


@decorator_without_even
def my_list(any_list):
    print(any_list)


def main():
    list01 = [1, 2, 3, 4, 5, 6]
    my_list(list01)


if __name__ == '__main__':
    main()
