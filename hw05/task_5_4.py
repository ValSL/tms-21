'''4) Для заданного числа N составьте программу вычисления суммы
S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число. [02-3.2-ML21]
'''

n = 5
index = 1
s = 0
while index <= 5:
    s = s + 1/index
    index += 1

print(s)