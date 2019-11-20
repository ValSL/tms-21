def list_sum(any_list):
    number_sum = 0
    for number in any_list:
        number_sum += number
    return number_sum


def main():
    A = [1, -2, 3, -7, 2, 8, -11]
    negative_list = [number for number in A if number < 0]
    positive_list = [number for number in A if number > 0]
    print(list_sum(negative_list))
    print(list_sum(positive_list))


if __name__ == "__main__":
    main()
