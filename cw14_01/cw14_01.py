import argparse
import csv
import os
from datetime import timedelta, datetime
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('name', type=str)
parser.add_argument('sec_name', type=str)
parser.add_argument('hours', type=int)
parser.add_argument('minutes', type=int)
parser.add_argument('seconds', type=int)
args = parser.parse_args()


def timer_generator(hours, minutes, sec):
    h_to_sec = hours * 3600
    m_to_sec = minutes * 60
    seconds = sec + m_to_sec + h_to_sec
    b = timedelta(seconds=seconds)
    for i in range(seconds):
        yield str(b)
        b -= timedelta(seconds=1)


with open(f'{os.getcwd()}/cw14_01/log.csv', 'a') as f:
    csvwriter = csv.writer(f)
    date, time = str(datetime.today()).split(' ')
    csvwriter.writerow([args.name, args.sec_name, date, time])
timer = timer_generator(args.hours, args.minutes, args.seconds)

for i in timer:
    print(i)
    sleep(1)
print('ALARM!!!')
