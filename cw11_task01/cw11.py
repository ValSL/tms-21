class Dog:
    def bark(self):
        print('Woof Woof!')

    def jump(self):
        print('Jump')

    def run(self):
        print('Run')


def main():
    dog1 = Dog()
    dog2 = Dog()
    print(dog1, dog2)
    print('______________')
    dog1.jump()
    dog1.run()


if __name__ == '__main__':
    main()
