from datetime import datetime


def my_decorator(func):
    def func_time():
        time_before_func = datetime.now()
        func()
        time_after_func = datetime.now() - time_before_func
        print(time_after_func)
    return func_time


@my_decorator # не верно то что, func_time вызывается здесь!!! func_time просто перекрывает print_func
def print_func():
    print("Hello")


print_func()
