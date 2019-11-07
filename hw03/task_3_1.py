#Введите число. Если это число делиться на 1000 без остатка, то выведите на экран "millennium"

number01 = int(input("Enter: "))

if number01 % 1000 == 0:
    print("millennium")
