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
            print('%11s' % col, end='')
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


def csv_file_delete(csv_filename: str, pos=None):
    """Positional deletion of information from csv file"""
    lines = []
    with open(csv_filename, 'r') as my_file:
        csvreader = csv.reader(my_file)
        fields = next(csvreader)
        for line in csvreader:
            lines.append(line)
        if pos is None:
            lines.pop(len(lines) - 1)
            csv_write(fields, lines, csv_filename)
            return
        lines.pop(pos)
        csv_write(fields, lines, csv_filename)


def sum_of_all_goods(csv_filename: str):
    """Sum of all products in file"""
    lines = []
    with open(csv_filename, 'r') as f:
        csvreader = csv.reader(f)
        fields = next(csvreader)
        cost_sum = 0
        for line in csvreader:
            for index, elem in enumerate(line):
                if index == 1:
                    cost_sum += int(elem)
        return cost_sum


def most_expensive(csv_filename: str):
    with open(csv_filename, 'r') as f:
        csvreader = csv.reader(f)
        fields = next(csvreader)
        for index_line, line in enumerate(csvreader):
            for index, elem in enumerate(line):
                if index_line == 0:
                    max = int(line[1])
                if index == 1:
                    if int(elem) > max:
                        max = elem
        return max


def cheapest(csv_filename: str):
    with open(csv_filename, 'r') as f:
        csvreader = csv.reader(f)
        fields = next(csvreader)
        for index_line, line in enumerate(csvreader):
            for index, elem in enumerate(line):
                if index_line == 0:
                    min = int(line[1])
                if index == 1:
                    if int(elem) < min:
                        min = elem
        return min


def reducing_products_amount(csv_filename: str, prod_index: int, n=1):
    """Reducing the number of products"""
    lines = []
    with open(csv_filename, 'r') as f:
        csvreader = csv.reader(f)
        fields = next(csvreader)
        for line in csvreader:
            lines.append(line)
    for index, elem in enumerate(lines[prod_index]):
        if index == 2:
            line[index] = int(line[index]) - n

    csv_write(fields, lines, csv_filename)
