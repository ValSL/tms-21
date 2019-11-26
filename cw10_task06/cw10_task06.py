from random import randint
import json


def main():
    matrix = []
    for i in range(3):
        line = []
        for j in range(3):
            line.append(randint(1,9))
        matrix.append(line)    # ЭТО 10.7 доделать

    with open('file.json', 'a') as f:
        data = json.dumps({'matrix': matrix})
        f.write(data)

    with open('file2.json', 'w'):
        for row in matrix:
            for index, elem in enumerate(row):
                if elem % 2 == 0:
                    matrix[index] = 0
        data2 = json.dumps({'matrix': matrix})


if __name__ == '__main__':
    main()
