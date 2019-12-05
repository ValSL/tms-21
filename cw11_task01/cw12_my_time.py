class MyTime:
    def __init__(self, *args):
        if len(args) == 3:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif len(args) == 1 and isinstance(args[0], str):
            lst = args[0].split('-')
            self.hours = int(lst[0])
            self.minutes = int(lst[1])
            self.seconds = int(lst[2])
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
        return not self == other  # Вызывается __eq__

    def __ge__(self, other):
        return self.hours >= other.hours and self.minutes >= other.minutes and self.seconds >= other.seconds

    def __le__(self, other):
        return self.hours <= other.hours and self.minutes <= other.minutes and self.seconds <= other.seconds

    def __gt__(self, other):
        return self.hours > other.hours and self.minutes > other.minutes and self.seconds > other.seconds

    def __lt__(self, other):
        return self.hours < other.hours and self.minutes < other.minutes and self.seconds < other.seconds

    def __mul__(self, other):
        mul_h = self.hours * other
        mul_m = self.minutes * other
        mul_s = self.seconds * other
        return MyTime(mul_h, mul_m, mul_s)

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
        self.minutes += self.seconds // 60
        self.seconds = self.seconds % 60
        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60
        return f'{self.hours}:{self.minutes}:{self.seconds}'


def main():
    my_time = MyTime(12, 90, 3601)
    my_time2 = MyTime(4, 234, 5000)
    print(my_time < my_time2) # fix


if __name__ == '__main__':
    main()
