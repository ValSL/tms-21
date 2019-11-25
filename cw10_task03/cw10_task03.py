def main():
    with open('task03.txt', 'a') as f:
        counter = 0
        while counter < 3:
            line = input("line ")
            f.write(f'{line}\n')
            counter += 1


if __name__ == '__main__':
    main()
