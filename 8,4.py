a = float(input("Введите a (0 < a <= 1): "))
znam = 1
while True:
    value = 1.0 / znam
    if value < a:
        print(f"Первое число меньше {a}: 1/{znam} = {value:.3f}")
        break
    znam += 1
