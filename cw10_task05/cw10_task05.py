def main():
    with open('task05.txt', 'r') as f:  # Можно открывать сразумного файлов ,open() as a, open() as b, ...
        for index, line in enumerate(f.readlines()):
            if (index + 1) % 2 == 0:
                f2 = open('file2.txt', 'a')
                f2.write(f'{line}\n')
                f2.close()
            elif (index + 1) % 2 != 0:
                f3 = open('file3.txt', 'a')
                f3.write(f'{line}\n')
                f3.close()


if __name__ == '__main__':
    main()
