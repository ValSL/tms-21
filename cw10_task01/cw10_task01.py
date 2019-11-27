def print_first_line():
    f = open('test.txt')
    print(f.readline())
    f.close()


def print_fifth_line():
    f = open('test.txt')
    for i in range(1, 6):
        f.readline()
        if i == 4:
            print(f.readline())
    f.close()


def print_five_lines():
    f = open('test.txt')
    for line in range(1, 6):
        print(f.readline().strip())
    f.close()


def print_certain_lines(a, b):
    f = open('test.txt')
    index = 1
    counter = 0
    while True:
        line = f.readline()
        counter += 1
        if not line:
            break
        if b >= counter >= a:
            print(line)
    f.close()


def print_all_file():
    f = open('test.txt')
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
