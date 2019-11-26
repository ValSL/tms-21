def main():
    with open('file1.txt', 'r') as f1:
        with open('file2.txt', 'r') as f2:
            lst01 = f1.readlines()
            lst02 = f2.readlines()
            index = 0
            while index < len(lst01):
                if lst01[index] != lst02[index]:
                    print(index + 1)
                index += 1


if __name__ == '__main__':
    main()
