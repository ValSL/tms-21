import csv
from datetime import datetime, date, time, timedelta


def main():
    fields = ['Date', 'Place', 'Degrees', 'Wind_speed']
    rows = [
        [date(2019, 11, 26), 'Minsk', '3', '10'],
        [date(2019, 11, 25), 'Mogilev', '4', '11'],
        [date(2019, 11, 24), 'Gomel', '5', '12'],
        [date(2019, 11, 23), 'Minsk', '1', '9'],
        [date(2019, 11, 22), 'Minsk', '4', '15'],
        [date(2019, 11, 21), 'Grodno', '6', '8'],
        [date(2019, 11, 20), 'Minsk', '5', '12'],
        [date(2019, 11, 19), 'Vitebsk', '2', '14'],
        [date(2019, 11, 18), 'Minsk', '7', '4'],
    ]
    with open('f.csv', 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    with open('f.csv', 'r') as f:
        delta = timedelta(7)
        weather = [0, 0] # [Температура, Скорость ветра]
        count = 0
        lines = []
        csvreader = csv.reader(f)
        fields = next(csvreader)
        for line in csvreader:
            lines.append(line)

        for line in lines:
            a = datetime.strptime(line[0], '%Y-%m-%d').date()
            if line[1] == 'Minsk' and date.today() - a <= delta:
                weather[0] += int(line[2])
                weather[1] += int(line[3])
                count += 1
        avg_temp = weather[0] / count
        avg_speed = weather[1] / count
        print(avg_temp)
        print(avg_speed)


if __name__ == '__main__':
    main()
