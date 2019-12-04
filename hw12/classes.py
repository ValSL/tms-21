class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    pass


class Circle(Figure):
    def __init__(self, center: Point, radius: int):
        self.center = center
        self.radius = radius

    def perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter

    def square(self):
        square = 3.14 * (self.radius) ** 2
        return square


class Traingle(Figure):
    def __init__(self, x: Point, y: Point, z: Point):
        self.traingle_x = x
        self.traingle_y = y
        self.traingle_z = z

    def sides_of_traingle(self):
        xy = ((self.traingle_x.x - self.traingle_y.x) ** 2 + (self.traingle_x.y - self.traingle_y.y) ** 2) ** 0.5
        yz = ((self.traingle_y.x - self.traingle_z.x) ** 2 + (self.traingle_y.y - self.traingle_z.y) ** 2) ** 0.5
        xz = ((self.traingle_x.x - self.traingle_z.x) ** 2 + (self.traingle_x.y - self.traingle_z.y) ** 2) ** 0.5
        return xy, yz, xz

    def perimeter(self):
        xy, yz, xz = Traingle.sides_of_traingle(self)
        per = xy + yz + xz
        return per

    def square(self):
        xy, yz, xz = Traingle.sides_of_traingle(self)
        half_perimeter = (Traingle.perimeter(self)) / 2
        square = (half_perimeter * (half_perimeter - xy) * (half_perimeter - yz) * (half_perimeter - xz)) ** 0.5
        return square


class Square(Figure):
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def square(self):
        side = self.a.x - self.b.x
        return side ** 2

    def perimeter(self):
        side = self.a.x - self.b.x
        return side * 4


