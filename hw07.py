'''Написать 12 функций по переводу:'''

'''Дюймы в сантиметры'''
def inches_to_centimeters(inches):
    cent = inches * 2.54
    return cent


a = inches_to_centimeters(54)



'''Сантиметры в дюймы'''
def centimeters_to_inches(cent):
    inch = cent * 0.39
    return inch


a = centimeters_to_inches(220)



'''Мили в километры'''
def miles_in_kilometers(miles):
    kil = miles * 1.61
    return kil


a = miles_in_kilometers(13)



'''Километры в мили'''
def kilometers_in_miles(kil):
    miles = kil * 0.62
    return miles


a = kilometers_in_miles(14)



'''Фунты в килограммы'''
def pounds_to_kilograms(pound):
    kilo = pound * 0.45
    return kilo


a = pounds_to_kilograms(17)



'''Килограммы в фунты'''
def kilograms_to_pounds(kilo):
    pound = kilo * 2.2
    return pound


a = kilograms_to_pounds(19)



'''Унции в граммы'''
def ounces_to_grams(oun):
    gram = oun * 28.35
    return gram


a = ounces_to_grams(14)



'''Граммы в унции'''
def grams_to_ounces(gram):
    oun = gram * 0.035
    return oun


a = grams_to_ounces(12)



'''Галлон в литры'''
def gallon_to_liter(gal):
    lit = gal * 3.79
    return lit


a = gallon_to_liter(18)



'''Литры в галлоны'''
def liter_to_gallon(lit):
    gal = lit * 0.26
    return gal


a = liter_to_gallon(15)



'''Пинты в литры'''
def pints_to_liter(pin):
    lit = pin * 0.47
    return lit


a = pints_to_liter(13)



'''Литры в пинты'''
def liter_to_pints(lit):
    pin = lit * 2.11
    return pin


a = liter_to_pints(14)


dict01 = {
    1: "Дюймы в сантиметры",
    2: "Сантиметры в дюймы",
    3: "Мили в километры",
    4: "Километры в мили",
    5: "Фунты в килограммы",
    6: "Килограммы в фунты",
    7: "Унции в граммы",
    8: "Граммы в унции",
    9: "Галлон в литры",
    10: "Литры в галлоны",
    11: "Пинты в литры",
    12: "Литры в пинты",
}

while True:
    for index, value in dict01.items():
        print(f'{index} - {value}')
    variant = int(input("Выберите один из вариантов: "))
    if variant == 1:
        num = int(input("Введите число"))
        print(inches_to_centimeters(num))
    elif variant == 2:
        num = int(input("Введите число"))
        print(centimeters_to_inches(num))
    elif variant == 3:
        num = int(input("Введите число"))
        print(miles_in_kilometers(num))
    elif variant == 4:
        num = int(input("Введите число"))
        print(kilometers_in_miles(num))
    elif variant == 5:
        num = int(input("Введите число"))
        print(pounds_to_kilograms(num))
    elif variant == 6:
        num = int(input("Введите число"))
        print(kilograms_to_pounds(num))
    elif variant == 7:
        num = int(input("Введите число"))
        print(ounces_to_grams(num))
    elif variant == 8:
        num = int(input("Введите число"))
        print(grams_to_ounces(num))
    elif variant == 9:
        num = int(input("Введите число"))
        print(gallon_to_liter(num))
    elif variant == 10:
        num = int(input("Введите число"))
        print(liter_to_gallon(num))
    elif variant == 11:
        num = int(input("Введите число"))
        print(pints_to_liter(num))
    elif variant == 12:
        num = int(input("Введите число"))
        print(liter_to_pints(num))
    elif variant == 0:
        break
    else:
        print("Неверное число")
