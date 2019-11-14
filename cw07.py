import random


def matrix_create(n, m):
    matrix = []
    for row in range(n):
        mass_line = []
        for line in range(m):
            mass_line.append(random.randint(0, 9))
        matrix.append(mass_line)
    return matrix


def matrix_out(any_matrix):
    for line in any_matrix:
        print(line)


def matrix_sum(any_matrix):
    sum = 0
    for i in any_matrix:
        for j in i:
            sum += j
    return sum


def matrix_max(any_matrix):
    max = any_matrix[0][0]
    for i in any_matrix:
        for j in i:
            if j > max:
                max = j
    return max


def matrix_min(any_matrix):
    min = any_matrix[0][0]
    for i in any_matrix:
        for j in i:
            if j < min:
                min = j
    return min


n = int(input())
m = int(input())
matrix = matrix_create(n, m)

matrix_out(matrix)
print(matrix_sum(matrix))
print(matrix_max(matrix))
print(matrix_min(matrix))
print("a")
