class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('run')

    def jump(self):
        print('jump')

    def sleep(self):
        print('sleep')

    def birthday(self):
        self.age += 1


class Dog(Pet):
    def bark(self):
        print('bark')


class Cat(Pet):
    def meow(self):
        print('meow')


class Parrot(Pet):
    def fly(self):
        print('fly')

