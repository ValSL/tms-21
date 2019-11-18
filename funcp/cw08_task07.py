def is_power_n(k, n):
    number = 1
    for i in range(k+1):
        number = number * n
        if number == k:
            return True




def main():
    a = is_power_n(9, 2)
    print(a)


if __name__ == '__main__':
    main()
