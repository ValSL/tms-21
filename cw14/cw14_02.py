from time import sleep
import random


def infinite_numbers(a, b, diff):
    while True:
        yield random.randint(a, b)
        a += diff
        b += diff


def main():
    mg = infinite_numbers(1, 10, 100)

    for i in mg:
        print(i)
        sleep(1)


if __name__ == '__main__':
    main()
