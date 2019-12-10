from time import sleep
from random import randint


def my_gen():
    while True:
        yield randint(1, 9)


mg = my_gen()
for i in mg:
    print(i)
    sleep(1)