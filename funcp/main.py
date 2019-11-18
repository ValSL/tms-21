

def count_of_numbers(list):
    dict01 = {}
    for number in list:
        if number in dict01.keys():
            dict01[number] += 1
        else:
            dict01[number] = 1
    return dict01


def main():
    list_of_numbers = [1, 1, 1, 2, 2, 3]
    print(count_of_numbers(list_of_numbers))


if __name__ == '__main__':
    main()
