kmh = float(input("Введите скорость в км/ч: "))
ms = float(input("Введите скорость в м/с: "))
kmh_to_ms = kmh / 3.6
if kmh_to_ms > ms:
    print("Скорость в км/ч больше")
else:
    print("Скорость в м/с больше")
