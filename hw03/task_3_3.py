'''Ввести строку. Если длина строки больше 10 символов,
то создать новую строку с 3 восклицательными знаками в конце  ('!!!') и вывести на экран.
Если меньше 10, то вывести на экран второй символ строки
'''
str01 = input("Enter: ")

if len(str01) > 10:
    new_str = f"{str01}!!!"
    print(new_str)
else:
    print(str01[1])
