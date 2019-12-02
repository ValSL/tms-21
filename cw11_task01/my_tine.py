class MyTime:
    def __init__(self, *args):
        if len(args) == 3:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif len(args) == 1 and isinstance(args[0], str):
            lst = args[0].split('-')
            self.hours = lst[0]
            self.minutes = lst[1]
            self.seconds = lst[2]
        elif len(args) == 1 and isinstance(args[0], MyTime):
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds
        else:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __ne__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return False
        else:
            return True

    def __add__(self, other):
        sum_h = self.hours + other.hours
        sum_m = self.minutes + other.minutes
        sum_s = self.seconds + other.seconds
        return MyTime(sum_h, sum_m, sum_s)

    def __sub__(self, other):
        sum_h = self.hours - other.hours
        sum_m = self.minutes - other.minutes
        sum_s = self.seconds - other.seconds
        return MyTime(sum_h, sum_m, sum_s)

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'


def main():
    my_time = MyTime(1, 1, 1)
    my_time2 = MyTime()
    print(my_time2)


if __name__ == '__main__':
    main()
