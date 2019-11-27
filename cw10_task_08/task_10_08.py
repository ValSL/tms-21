from csv_utils import csv_write, csv_read, csv_file_add, csv_file_delete
import csv

fields = ['Product_name', 'Cost', 'Amount', 'Comment']
rows = [['house', '$13123', '1', 'App'], ['Fur_coat', '$423432', '3', 'Fur']]

csv_write(fields, rows, 'f.csv')
csv_read('f.csv')
print("___________________________________________")

csv_file_add('f.csv', ['Car', '$1000000', '3', 'Lamba'])
csv_read('f.csv')
print("___________________________________________")

csv_file_delete('f.csv', 2)
csv_read('f.csv')
