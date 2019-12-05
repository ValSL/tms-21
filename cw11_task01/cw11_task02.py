from random import randint, choice
from string import ascii_uppercase
from abc import ABC, abstractmethod


class Animal(ABC):
    pass


class WildAnimal(Animal):
    pass


class Lion(WildAnimal):
    pass


class Wolf(WildAnimal):
    pass


class Pet(Animal):
    __counter = 0
    x = 1

    def __init__(self, name, age, master, weight, height):
        self.weight = weight
        self.height = height
        self.name = name
        self.age = age
        self.master = master
        Pet.__counter += 1

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

    def jump(self, x):
        print(f'jump {x} meters')

    def sleep(self):
        print('sleep')

    def birthday(self):
        self.age += 1

    @abstractmethod
    def voice(self):
        pass

    @classmethod
    def get_counter(cls):
        return cls.__counter

    @staticmethod
    def get_random_name():
        return f'{choice(ascii_uppercase)}-{randint(1, 99)}'


class Horse(Pet):
    def voice(self):
        print('blabla')


class Donkey(Pet):
    def voice(self):
        print('lala')


class Mule(Donkey):
    pass


class Dog(Pet):
    def voice(self):
        print('bark')

    def jump(self, x):
        if x > 0.5:
            print('Dogs cannot jump so high!')
        else:
            super().jump(x)


class Cat(Pet):
    def voice(self):
        print('meow')

    def jump(self, x):
        if x > 2:
            print('Cats cannot jump so high!')
        else:
            super().jump(x)


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def fly(self):
        if self.weight > 0.1:
            print('This parrot cant fly')
        else:
            print('fly')

    def change_weight(self, weight=0.05):
        self.weight += weight

    def change_height(self, height=0.05):
        self.weight += height

    def jump(self, x):
        if x > 0.05:
            print('Parrots cannot jump so high!')
        else:
            super().jump(x)

    def voice(self):
        print('Anything')


def voice_call(animals: list):
    for animal in animals:
        animal.voice()


def main():
    parrot = Parrot('Vovchik', 3, 'Pasha', 0.01, 4, 'ara')
    dog = Dog('Bobik', 3, 'vovchik', 4, 5)
    cat = Cat('Murzik', 5, 'Pasha', 5, 6)
    parrot.change_weight()
    parrot.fly()
    print(parrot.weight)
    print('___________________________')

    dog.jump(3)
    parrot.jump(0.01)
    cat.jump(2)
    print(parrot.species)
    print('___________________________')

    animal_list = [parrot, cat, dog]
    voice_call(animal_list)
    print(dir(dog))
    print(Pet._Pet__counter)
    print('___________________________')
    print(Pet.get_counter())
    print(Pet.get_random_name())
    print('_____________________________')
    mule = Mule('Vova', 12, 'Pasha', 60, 15)
    mule.voice()
    print(mule.x)


if __name__ == '__main__':
    main()
