from matrix import Matrix


def main():
    matrix = Matrix(3, 3, 1, 9)
    print(matrix)
    print(f'max elem is {matrix.max_elem()}')
    print(f'min elem is {matrix.min_elem()}')
    print(f'sum of elems is {matrix.sum_elem()}')


if __name__ == '__main__':
    main()
