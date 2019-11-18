from typing import Optional, Union


def func(a: Union[int, float], b: Union[float, int], c: Union[float, int]) -> tuple:
    """Квадратное уравнение"""
    disc = (b ** 2) - 4 * a * c
    if disc < 0:
        print('Нет корней')
        res = 0
        return res
    elif disc == 0:
        res = -b / 2 * a
        return res
    else:
        res1 = (-b - (disc*0.5))/2 * a
        res2 = (-b + (disc*0.5))/2 * a
        return res1, res2


def main():
    print(func(3, 7, 2))


if __name__ == '__main__':
    main()
