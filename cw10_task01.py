def print_first_line():
    f = open('test.txt')
    print(f.readline())
    f.close()

def prinf_fifth_line():
    f = open('test.txt')
    for i in range(1, 6):
        f.readline()
        if i == 4:
            print(f.readline())
    f.close()


def print_five_lines():
    f = open('test.txt')
    for line in range(1, 5):
        print(f.readline())
    f.close()


