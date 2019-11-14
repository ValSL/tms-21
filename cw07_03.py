import random


def matrix_create(n, rand_from = 1, rand_to = 9):
    matrix = []
    for row in range(n):
        mass_line = []
        for line in range(n):
            mass_line.append(random.randint(rand_from, rand_to))
        matrix.append(mass_line)
    return matrix


print(matrix_create(3,1,20))
