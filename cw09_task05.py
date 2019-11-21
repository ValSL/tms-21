from functools import reduce


def main():
    filt = reduce(lambda a, x: x * a, filter(lambda num: num % 3 == 0, [1, 2, 3, 4, 5, 6]), 1)
    print(filt)


if __name__ == '__main__':
    main()
