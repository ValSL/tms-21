import funcs


def main():
    while True:
        print('''Выберите действие
        1) Добавить бренд
        2) Удалить бренд
        3) Обновить бренд
        4) Вывести бренды
        5) Добавить машину
        6) Удалить машину
        7) Вывести машины
        8) Обновить машину
        9) Создать базу
        0) Выход''')
        choose_dict = {
            1: funcs.add_brand,
            5: funcs.add_car,
            2: funcs.delete_brand,
            6: funcs.delete_car,
            3: funcs.update_brand,
            4: funcs.print_available_brands,
            9: funcs.create_base,
            7: funcs.print_cars,
            8: funcs.update_car,
        }
        choose = int(input('Enter number: '))
        if not choose:
            break
        action = choose_dict[choose]
        action()


if __name__ == '__main__':
    main()
