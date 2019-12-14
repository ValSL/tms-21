import functions

while True:
    print(''''Выберите действие:
1) Добавление в базу
2) Просмотр по id
3) Изменение по id
4) Удаление по id''')
    inp = input('Enter: ')
    if inp == '0':
        break
    elif inp == '1':
        functions.add_product()
        input('press enter')
    elif inp == '2':
        functions.show_product()
        input('press enter')
    elif inp == '3':
        functions.update_product()
        input('press enter')
    elif inp == '4':
        functions.delete_product()
        input('press enter')
    else:
        print('Неверный ввод!')
        input('press enter')

