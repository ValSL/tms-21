import sys

summ = 0
print(sys.argv)
for number in sys.argv[1:]:
    if number.isdigit():
        number = int(number)
        summ += number

print(summ)
