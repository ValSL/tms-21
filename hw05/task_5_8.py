'''8) В заданной строке расположить в обратном порядке все слова.
 Разделителями слов считаются пробелы. [02-7.2-HL08]
'''

str01 = input()
splited_str = str01.split()
splited_str.reverse()
str02 = ' '.join(splited_str)
print(str02)

