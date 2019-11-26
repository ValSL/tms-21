from csv_utils import csv_write, csv_read, csv_file_add
import csv

fields = ['one', 'two', 'three']
rows = [[1, 2, 3], ['q', 'w', 'e'], ['P', 'O', 'A']]
csv_write(fields, rows)
csv_read('new_file.csv')
csv_file_add('new_file.csv', ['b', 'b', 'b'], 5)
csv_read('new_file.csv')
