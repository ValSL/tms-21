from sqlalchemy.orm import sessionmaker
from hw16_db_connect import engine
from hw16_db_connect import Base
import funcs


def main():
    while True:
        print('''Выберите действие
        1) Добавить бренд
        2) Добавить машину
        3) Удалить бренд
        4) Удалить машину
        5) Создать базу''')
        choose_dict = {
            1: funcs.add_brand,
            2: funcs.add_car,
            3: funcs.delete_brand,
            4: funcs.delete_car,
            5: funcs.create_base,
        }
        choose = int(input('Enter number: '))
        if not choose:
            break
        action = choose_dict[choose]
        action()


if __name__ == '__main__':
    main()
