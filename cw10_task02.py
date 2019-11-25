def main():
    with open('task02.txt', 'w') as f:
        counter = 0
        while counter < 6:
            line = input('line ')
            f.write(f'{line}\n')
            counter += 1


if __name__ == '__main__':
    main()
