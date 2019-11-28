class Pet:
    def __init__(self, name, age, master, weight, height):
        self.weight = weight
        self.height = height
        self.name = name
        self.age = age
        self.master = master

    def change_weight(self, weight=None):
        if weight:
            self.weight += weight
        else:
            self.weight += 0.2

    def change_height(self, height=None):
        if height:
            self.weight += height
        else:
            self.weight += 0.2

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
        if self.weight > 0.1:
            print('This parrot cant fly')
        else:
            print('fly')


parrot = Parrot('Vovchik', 3, 'Pasha', 0.01, 4)
parrot.change_weight()
parrot.fly()

