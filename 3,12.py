flat = int(input("Введите номер квартиры: "))
flats_per_floor = 4
floor = (flat - 1) // flats_per_floor + 1
position_on_floor = (flat - 1) % flats_per_floor + 1
print("Этаж:", floor)
print("Порядковый номер на этаже:", position_on_floor)
