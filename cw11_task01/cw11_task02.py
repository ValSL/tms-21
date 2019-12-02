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

    def jump(self, x):
        print(f'jump {x} meters')

    def sleep(self):
        print('sleep')

    def birthday(self):
        self.age += 1

    def voice(self):
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
    print('_____________________________')

    dog.jump(3)
    parrot.jump(0.01)
    cat.jump(2)
    print(parrot.species)
    print('____________________')

    animal_list = [parrot, cat, dog]
    voice_call(animal_list)
    print(dir(dog))

if __name__ == '__main__':
    main()
