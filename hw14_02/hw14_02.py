import argparse
from datetime import timedelta, datetime

parser = argparse.ArgumentParser()
parser.add_argument('focus_time', default=timedelta(minutes=25))
parser.add_argument('chill_time', default=timedelta(minutes=5))
parser.add_argument('loop_count', default=4)
parser.add_argument('task_name', default='new_task')
args = parser.parse_args()

def pomodoro_timer(focus_time, chill_time, loop_time):