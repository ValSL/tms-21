import csv
from datetime import datetime, date, time
from random import randint


def csv_write(fields: list, lines: list, name='users.csv'):
    with open(name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(lines)

def csv_read(csv_filename: str):
    rows = []
    with open(csv_filename, 'r') as my_file:
        csvreader = csv.reader(my_file)
        fields = next(csvreader)
        for line in csvreader:
            rows.append(line)
    return fields, rows

def main():
    pass



if __name__ == '__main__':
    main()
