cars = [{'serial_number': 1, 'year': 1998}, {'serial_number': 2, 'year': 2001}]

list02 = [car for car in cars if car['year'] > 2000]

print(list02)
