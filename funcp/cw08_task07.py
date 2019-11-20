def is_power_n(k, n):
    number = 1
    for i in range(k+1):
        number = number * n
        if number == k:
            return True
    return False


def main():
    n = 2
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = 0
    for number in numbers:
        res = is_power_n(number, n)
        if res == True:
            count += 1
        else:
            continue
    print(f'Количество степене числа {n} в списке, равно {count}')


if __name__ == '__main__':
    main()
