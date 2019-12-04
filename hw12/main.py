from classes import Circle, Traingle, Square, Point


def main():
    lst01 = [Circle(Point(3, 5), 6), Traingle(Point(2, 3), Point(5, 9), Point(7, 8)), Square(Point(6, 2), Point(8, 4))]
    for figure in lst01:
        print(figure.square())


if __name__ == '__main__':
    main()
