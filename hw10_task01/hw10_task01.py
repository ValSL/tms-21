import csv

def main():
    fields = ['Name', 'Second_name', 'Age']
    rows = [
        ['Ivan', 'Ivanov', 8],
        ['Peter', 'Petrov', 7],
        ['Denis', 'Denisov', 15],
        ['Sidor', 'Sidorov', 50],
        ['Oleg', 'Olegov', 30]
    ]
    with open('f.csv', 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    with open('f.csv', 'r') as f:
        ages = []
        csvreader = csv.reader(f)
        file_fields = next(csvreader)
        for line in csvreader:
            for index, age in enumerate(line):
                if index == 2:
                    ages.append(int(age))
        with open('f_report.csv', 'w') as f2:
            new_fields = ['1-12', '13-18', '19-25', '26-40', '40+']
            new_rows = [[0, 0, 0, 0, 0]]
            for num in ages:
                if 12 >= num >= 1:
                    new_rows[0][0] += 1
                elif 18 >= num >= 13:
                    new_rows[0][1] += 1
                elif 25 >= num >= 19:
                    new_rows[0][2] += 1
                elif 40 >= num >= 26:
                    new_rows[0][3] += 1
                elif num > 40:
                    new_rows[0][4] += 1
            csvwriter = csv.writer(f2)
            csvwriter.writerow(new_fields)
            csvwriter.writerows(new_rows)


if __name__ == '__main__':
    main()
