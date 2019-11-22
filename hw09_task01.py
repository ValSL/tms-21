'''Дан список строк.
Отформатировать все строки в формате ‘{i} - {string}’, где i это порядковый номер строки в списке.
Использовать генератор списков.'''


def main():
    strings = ['first', 'second', 'third']

    new_lst = [f'{string_index + 1} - {string}' for string_index, string in enumerate(strings)]
    print(new_lst)


if __name__ == '__main__':
    main()
