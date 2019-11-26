import csv


def csv_write(fields: list, rows: list, filename='new_file.csv'):
    """Create csv file"""
    with open(filename, 'w') as my_file:
        csvwriter = csv.writer(my_file)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


def csv_read(csv_filename: str):
    """Console csv file output"""
    rows = []
    with open(csv_filename, 'r') as my_file:
        csvreader = csv.reader(my_file)
        fields = next(csvreader)
        for line in csvreader:
            rows.append(line)
    for col in fields:
        print('%10s' % col, end='')
    print()
    for line in rows:
        for col in line:
            print('%10s' % col, end='')
        print()


def csv_file_add(csv_filename: str, info: list, pos=None):
    """Positional addition of information to csv file"""
    lines = []
    with open(csv_filename, 'r') as my_file:
        csvreader = csv.reader(my_file)
        fields = next(csvreader)
        for line in csvreader:
            lines.append(line)
    if pos is None:
        lines.insert(len(lines), info)
        csv_write(fields, lines, csv_filename)
        return
    lines.insert(pos, info)

    csv_write(fields, lines, csv_filename)






