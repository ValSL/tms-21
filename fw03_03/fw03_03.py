
def main():
    print('''Выберите вайловую систему
            1) JSON
            2) CSV''')
    choose = input('Enter: ')
    if choose == '1':
        fw01_01.main()
    elif choose == '2':
        fw01_02.main()


if __name__ == '__main__':
    main()
