k = int(input("Введите номер квартиры: "))
flats_per_floor = 6
floors = 9
entrances = 4
flats_per_entrance = floors * flats_per_floor
entrance = (k - 1) // flats_per_entrance + 1
flat_in_entrance = (k - 1) % flats_per_entrance + 1
floor = (flat_in_entrance - 1) // flats_per_floor + 1
position = (flat_in_entrance - 1) % flats_per_floor + 1
print("Подъезд:", entrance)
print("Этаж:", floor)
print("Порядковый номер на этаже:", position)
