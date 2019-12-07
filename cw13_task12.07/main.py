from matrix import Matrix


def main():
    matrix = Matrix(3, 3, 1, 9)
    print(matrix)
    print(matrix.max_elem())
    print(matrix.min_elem())
    print(matrix.sum_elem())


if __name__ == '__main__':
    main()
