def my_func(*args):
    sum_res = 0
    max_number = args[0]
    for i in args:
        sum_res += i
        if i > max_number:
            max_number = i
    return sum_res, max_number


max_num, sum_of_numbers = my_func(1, 2, 3, 4, 5, -7)
print(max_num)
print(sum_of_numbers)
