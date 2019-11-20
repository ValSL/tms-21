def fact(number):
    res = 1
    for i in range(1, number + 1):
        res = i * res
    return res


def sin1(x, e):
    sin_x = x
    while True:
        for n in range(1, 100):
            slag = (-1)**n * x**((2*n+1)/fact(2*n+1))
            if slag > e:
                sin_x += slag
            else:
                continue
        return sin_x


def main():
    print(sin1(4, -1))


if __name__ == "__main__":
    main()
