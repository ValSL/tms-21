def calc(x):
    res = ((x**(1/2)) + x)/2
    return res


def main():
    x = calc(5) + calc(12) + calc(19)
    print(x)


if __name__ == '__main__':
    main()
