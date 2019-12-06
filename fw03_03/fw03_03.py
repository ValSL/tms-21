from settings import ENGIN
from fw01_01 import fw01_01
from fw01_02 import fw01_02


def main():
    if ENGIN == 'JSON':
        print('Выбран JSON формат')
        input('press enter')
        fw01_01.main()
    elif ENGIN == 'CSV':
        print('Выбран CSV формат')
        input('press enter')
        fw01_02.main()


if __name__ == '__main__':
    main()
