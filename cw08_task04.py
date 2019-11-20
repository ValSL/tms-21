'''cw08 task 8.4'''

list_of_numbers = [1, 1, 2, 2, 2, 2, 3, 3, 3]
dict01 = {}

for number in list_of_numbers:
    if number in dict01:
        dict01[number] += 1
    else:
        dict01[number] = 1

for key, value in dict01.items():
    print(f'Цифр {key} в списке {value} ')

