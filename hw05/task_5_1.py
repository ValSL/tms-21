'''1) Написать программу, в которой вводятся два операнда Х и Y и знак операции sign (+, –, /, *).
 Вычислить результат Z в зависимости от знака.
 Предусмотреть реакции на возможный неверный знак операции, а также на ввод Y=0 при делении.
 Организовать возможность многократных вычислений без перезагрузки программа (т.е. построить бесконечный цикл).
 В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0').
'''

while True:
    x = int(input("Певрое число: "))
    y = int(input("Второе число: "))
    sign = input("Знак: ")
    z = 0
    if sign == "0":
        break
    if sign != "+" and sign != "-" and sign != "/" and sign != "*":
        print("Неверный знак!")
    elif sign == "+":
        z = x + y
        print(z)
    elif sign == "-":
        z = x - y
        print(z)
    elif sign == "*":
        z = x * y
        print(z)
    elif sign == "/":
        if y == 0:
            print("Деление на 0!")
        else:
            z = x / y
            print(z)

