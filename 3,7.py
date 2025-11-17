flat = int(input("Введите номер квартиры: "))
flats_per_floor = 3
floor = (flat - 1) // flats_per_floor + 1
print("Квартира находится на этаже №", floor)
