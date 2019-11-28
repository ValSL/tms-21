class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def bark(self):
        print('Woof Woof!')

    def jump(self):
        print('Jump')

    def run(self):
        print('Run')


def main():
    dog1 = Dog(2, 50, 'Barsik', 5)
    print(dog1)
    print('______________')

    dog1.jump()
    dog1.run()
    dog1.bark()


if __name__ == '__main__':
    main()
