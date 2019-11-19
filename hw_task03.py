def fact(number):
    res = 1
    for i in range(1, number + 1):
        res = i * res
    return res


def sin1(x, e):
    sin_x = 1
    for n in range(1, 6):
        sin_x += ((-1)**n) * (((-1) ** n) * (x**((2*n+1)/(fact(2*n+1)))))
    return sin_x


def main():
    print(sin1(1, 3))


if __name__ == "__main__":
    main()
