from datetime import datetime, date, time, timedelta

# a = datetime(2019, 10, 20, 20, 20, 20)
# print(a)
# delta = timedelta(7)
#
# if datetime.today() - a > delta:
#     print('aga')
str01 = '2019-4-2'
d = datetime.strptime(str01, '%Y-%m-%d')
print(d)
