'''2) Дано число. Найти сумму и произведение его цифр.'''
number = input("Число: ")
number_len = len(number) - 1
i = 0
res = int(number[0])
res2 = int(number[0])

while i < number_len:
    res += int(number[i+1])
    res2 *= int(number[i+1])
    i += 1

print(f"Сумма {res}")
print(f"Произвдение {res2}")


