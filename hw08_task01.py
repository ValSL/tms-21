'''Описать функцию fact2( n ) вещественного типа, вычисляющую двойной факториал :
n!! = 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное
(n > 0 — параметр целого типа.
С помощью этой функции найти двойные факториалы пяти данных целых чисел [01-11.2-Proc35]
'''


def fact2(n: int) -> int:
    """factorial calculation on even and odd numbers"""
    res = 1
    if n % 2 == 0:
        even_list = [i for i in range(1, n+1) if i % 2 == 0]
        for i in even_list:
            res = res * i
        return res
    if not n % 2 == 0:
        not_even_list = [i for i in range(1, n + 1) if not i % 2 == 0]
        for i in not_even_list:
            res = res * i
        return res


def main():
    numbers = [5, 6, 9, 12, 15]
    for i in numbers:
        print(fact2(i))


if __name__ == '__main__':
    main()

