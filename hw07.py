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
