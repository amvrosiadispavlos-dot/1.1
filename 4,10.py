km = float(input("Введите расстояние в километрах: "))
feet = float(input("Введите расстояние в футах: "))
km_to_m = km * 1000
feet_to_m = feet * 0.3048
if km_to_m < feet_to_m:
    print("Расстояние в километрах меньше")
else:
    print("Расстояние в футах меньше")
