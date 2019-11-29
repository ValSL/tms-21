import json
from datetime import datetime, date, time, timedelta
with open('test.json', 'w') as my_file:
   data = json.dumps({'a': 5})
   my_file.write(data)

with open('test.txt') as my_file:
   data = json.loads(my_file.read())
   list_keys = data
   list = dict(list_keys)
   print(list)


date = date(2018, 5, 3)
date_str = '28.11.2019'
a = datetime.strptime(date_str, '%d.%m.%Y').date()
print(a)




