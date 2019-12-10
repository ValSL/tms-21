import argparse
from datetime import timedelta, datetime
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('focus_time', type=int)
parser.add_argument('chill_time', type=int)
parser.add_argument('loop_count', type=int)
parser.add_argument('task_name')
args = parser.parse_args()


# def timer_generator(hours, minutes, sec):
#     h_to_sec = hours * 3600
#     m_to_sec = minutes * 60
#     seconds = sec + m_to_sec + h_to_sec
#     b = timedelta(seconds=seconds)
#     for i in range(seconds):
#         yield str(b)
#         b -= timedelta(seconds=1)
#
#
# with open(f'{os.getcwd()}/cw14_01/log.csv', 'a') as f:
#     csvwriter = csv.writer(f)
#     date, time = str(datetime.today()).split(' ')
#     csvwriter.writerow([args.name, args.sec_name, date, time])
# timer = timer_generator(args.hours, args.minutes, args.seconds)
#
# for i in timer:
#     print(i)
#     sleep(1)
# print('ALARM!!!')
#


def pomodoro_timer(focus_time, chill_time, loop_count):
    for j in range(loop_count):
        m_to_sec = focus_time * 60
        b = timedelta(seconds=m_to_sec)
        for i in range(m_to_sec):
            yield str(b)
            b -= timedelta(seconds=1)
        print('CHILL TIME')
        m_to_sec2 = chill_time * 60
        b2 = timedelta(seconds=m_to_sec2)
        for i in range(m_to_sec2):
            yield str(b2)
            b2 -= timedelta(seconds=1)
        if j != 3:
            print('WORK TIME')
    print('LONG CHILL TIME')



timer = pomodoro_timer(args.focus_time, args.chill_time, args.loop_count)

for i in timer:
    print(i)
    sleep(0.01)
