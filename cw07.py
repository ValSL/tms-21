import random

def matrix_create (n, m):
    matrix = []
    for row in range(n):
        mass_line = []
        for line in range(m):
            mass_line.append(random.randint(0, 9))
        matrix.append(mass_line)
    return matrix

print(matrix_create(3,3))