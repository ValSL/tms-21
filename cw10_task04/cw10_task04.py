def main():
    with open('task04.txt', 'r') as f:
        file_1 = f.readlines()

        for line in file_1:
            new_line = ''
            for index, elem in enumerate(line):
                if elem == '0':
                    new_line = new_line + '1'
                elif elem == '1':
                    new_line = new_line + '0'
                else:
                    new_line = new_line + elem

            f2 = open('new_file', 'a')
            f2.write(f'{new_line}\n')


if __name__ == '__main__':
    main()
