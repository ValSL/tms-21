from csv_utils import csv_write, csv_read, csv_file_add, csv_file_delete
import csv

fields = ['one', 'two', 'three']
rows = [[1, 2, 3], ['q', 'w', 'e'], ['P', 'O', 'A']]
csv_write(fields, rows)
csv_read('new_file.csv')
print('___________________________________')
csv_file_add('new_file.csv', ['b', 'b', 'b'], 1)
csv_read('new_file.csv')
print('___________________________________')
csv_file_delete('new_file.csv')
csv_read('new_file.csv')
