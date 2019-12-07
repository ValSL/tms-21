from random import randint


class Matrix:

    def __init__(self, n=5, m=5, a=0, b=0):
        self.data = [[randint(a, b) for i in range(n)] for j in range(m)]

    def __str__(self):
        return str(self.data)


    def max_elem(self):
        max_elem = self.data[0][0]
        for line in self.data:
            for row in line:
                if row > max_elem:
                    max_elem = row
        return max_elem

    def min_elem(self):
        min_elem = self.data[0][0]
        for line in self.data:
            for row in line:
                if row < min_elem:
                    max_elem = row
        return min_elem

    def sum_elem(self):
        sum_elem = 0
        for line in self.data:
            for row in line:
                sum_elem += row
        return sum_elem
