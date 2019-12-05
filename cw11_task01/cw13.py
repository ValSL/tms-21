from abc import ABC, abstractmethod


class Feline(ABC):
    @abstractmethod
    def scratch(self):
        pass


class Celine(ABC):
    @abstractmethod
    def swim(self):
        pass


class Animal(ABC):
    __counter = 0

    def __init__(self, name, age, master, weight, height):
        self.weight = weight
        self.height = height
        self.name = name
        self.age = age
        self.master = master
        Animal.__counter += 1

        @abstractmethod
        def voice():
            pass


class WildAnimal(Animal):
    def voice(self):
        pass


class Lion(WildAnimal, Feline):
    def voice(self):
        pass

    def scratch(self):
        print('scratch')


class Wolf(WildAnimal, Celine):
    def voice(self):
        pass

    def swim(self):
        print('swim')


class Pet(Animal):
    def voice(self):
        pass


class Horse(Pet):
    def voice(self):
        print('blabla')


class Donkey(Pet):
    def voice(self):
        print('lala')


class Mule(Donkey):
    def voice(self):
        pass


class Dog(Pet, Celine):
    def voice(self):
        print('bark')

    def swim(self):
        print('swim')


class Cat(Pet, Feline):
    def voice(self):
        print('meow')

    def scratch(self):
        print('scratch')


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def voice(self):
        print('Anything')


l = Lion('name', 4, 'asd', 4, 5)
