'''Написать 12 функций по переводу:'''

'''Дюймы в сантиметры'''
def inches_to_centimeters(inches):
    cent = inches * 2.54
    return cent


a = inches_to_centimeters(54)
print(a)


'''Сантиметры в дюймы'''
def centimeters_to_inches(cent):
    inch = cent * 0.39
    return inch


a = centimeters_to_inches(220)
print(a)


'''Мили в километры'''
def miles_in_kilometers(miles):
    kil = miles * 1.61
    return kil


a = miles_in_kilometers(13)
print(a)


'''Километры в мили'''
def kilometers_in_miles(kil):
    miles = kil * 0.62
    return miles


a = kilometers_in_miles(14)
print(a)


'''Фунты в килограммы'''
def pounds_to_kilograms(pound):
    kilo = pound * 0.45
    return kilo


a = pounds_to_kilograms(17)
print(a)


'''Килограммы в фунты'''
def kilograms_to_pounds(kilo):
    pound = kilo * 2.2
    return pound


a = kilograms_to_pounds(19)
print(a)


'''Унции в граммы'''
def ounces_to_grams(oun):
    gram = oun * 28.35
    return gram


a = ounces_to_grams(14)
print(a)


'''Граммы в унции'''
def grams_to_ounces(gram):
    oun = gram * 0.035
    return oun


a = grams_to_ounces(12)
print(a)


'''Галлон в литры'''
def gallon_to_liter(gal):
    lit = gal * 3.79
    return lit


a = gallon_to_liter(18)
print(a)


'''Литры в галлоны'''
def liter_to_gallon(lit):
    gal = lit * 0.26
    return gal


a = liter_to_gallon(15)
print(a)


'''Пинты в литры'''
def pints_to_liter(pin):
    lit = pin * 0.47
    return lit

a = pints_to_liter(13)
print(a)
