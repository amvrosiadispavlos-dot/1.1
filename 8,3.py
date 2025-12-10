a = float(input("Введите a (0 < a <= 1): "))
znam = 1
value = 1.0
while value >= a:
    print(f"1/{znam} = {value:.3f}")
    znam += 1
    value = 1.0 / znam
a = float(input("Введите a (0 < a <= 1): "))
for znam in range(1, 1000):
    value = 1.0 / znam
    if value < a:
        break
    print(f"1/{znam} = {value:.3f}")
