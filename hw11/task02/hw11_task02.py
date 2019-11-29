class Car:
    def __init__(self, brand, model, year, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    def increace_speed(self):
        self.__speed += 5

    def reduce_speed(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def show_speed(self):
        print(self.__speed)

    def reverse(self):
        self.__speed *= -1