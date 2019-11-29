'''Создать пять классов описывающие реальные объекты.
Каждый класс должен содержать минимум три приватных атрибута,
конструктор, геттеры и сеттеры для каждого атрибута, два метода.
'''


class Table:
    def __init__(self, material, weight, stability):
        self.__material = material
        self.__weight = weight
        self.__stability = stability

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material):
        self.__material = material

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def stability(self):
        return self.__stability

    @stability.setter
    def stability(self, stability):
        self.__stability = stability

    def crack(self):
        print('a crack appeared')

    def fall_over(self):
        print('The table fell')


class Car:
    def __init__(self, speed, weight, brand):
        self.__speed = speed
        self.__weight = weight
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight


    def turn_on(self):
        print('engine started')

    def turn_off(self):
        print('Engine off')


class House:
    def __init__(self, place, age, height):
        self.__height = height
        self.__age = age
        self.__place = place

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, place):
        self.__place = place

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def to_stand(self):
        print('the house stands')

    def ages(self):
        print('The house is getting old')


class Planet:
    def __init__(self, age, surface_area, distance_from_earth):
        self.__age = age
        self.__surface_area = surface_area
        self.__distance_from_earth = distance_from_earth

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def surface_area(self):
        return self.__surface_area

    @surface_area.setter
    def surface_area(self, surface_area):
        self.__surface_area = surface_area

    @property
    def distance_from_earth(self):
        return self.__distance_from_earth

    @distance_from_earth.setter
    def distance_from_earth(self, distance_from_earth):
        self.__distance_from_earth = distance_from_earth

    def spins(self):
        print('spinning around an axis')

    def explosion(self):
        print('Boom!')


class Hospital:
    def __init__(self, name, address, reputation):
        self.__name = name
        self.__address = address
        self.__reputation = reputation

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def reputation(self):
        return self.__reputation

    @reputation.setter
    def reputation(self, reputation):
        self.__reputation = reputation

    def treat_patients(self):
        print('treat')

    def dismiss(self):
        print('dismiss employees')




