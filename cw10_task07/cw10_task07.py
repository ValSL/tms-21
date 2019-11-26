from random import randint
import json


def main():
    matrix = []
    for i in range(3):
        line = []
        for j in range(3):
            line.append(randint(1, 9))
        matrix.append(line)
    with open('file.json', 'w') as f1:
        f1.write(json.dumps({'matrix': matrix}))

    with open('file.json') as f2:
        data = json.loads(f2.read())
        for value in data.values():
            for line in value:
                for index, elem in enumerate(line):
                    if elem % 2 == 0:
                        line[index] = 0
        new_matrix = value
        with open('file2.json', 'w') as f2:
            data = json.dumps({'matrix': new_matrix})
            f2.write(data)


if __name__ == '__main__':
    main()
