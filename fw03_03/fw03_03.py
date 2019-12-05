from settings import ENGIN
from fw01_01 import fw01_01
from fw01_02 import fw01_02


def main():
    if ENGIN == 'JSON':
        fw01_01.main()
    elif ENGIN == 'CSV':
        fw01_02.main()


if __name__ == '__main__':
    main()
