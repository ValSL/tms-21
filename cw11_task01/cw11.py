class Dog:
    def __init__(self, height, weight, name, age, master, city='Minsk'):
        self.__city = city
        self.__master = master
        self.__height = height
        self.__weight = weight
        self.__name = name
        self.__age = age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    def bark(self):
        print('Woof Woof!')

    def jump(self):
        print('Jump')

    def run(self):
        print('Run')


def main():
    dog1 = Dog(2, 50, 'Barsik', 5, 'Vovchik')
    print(dog1)
    print('______________')

    dog1.jump()
    dog1.run()
    dog1.bark()
    print(dog1.age)
    print(dog1.weight)
    print(dog1.height)
    print(dog1.name)
    dog1.change_name('Bobik')
    print(dog1.name)

    print(dog1._Dog__master)  # Обход приватности
    a = dog1.get_master()
    print(a)

    dog_city = dog1.get_city()
    print(dog_city)


if __name__ == '__main__':
    main()
