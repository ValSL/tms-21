import csv
rows = []

with open('students_info.csv', 'r') as file1:
    csvreader = csv.reader(file1)
    fields = next(csvreader)
    for line in csvreader:
        rows.append(line)
    for field in fields:
        print('%10s' % field, end='')
    print()
    for line in rows:
        for col in line:
            print('%10s' % col, sep='', end='')
        print()
