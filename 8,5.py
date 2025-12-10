a = float(input("Введите a (1 < a <= 1.5): "))
n = 2
while True:
    value = 1 + 1.0 / n
    if value < a:
        break
    print(f"1 + 1/{n} = {value:.3f}")
    n += 1
a = float(input("Введите a (1 < a <= 1.5): "))
for n in range(2, 1000):
    value = 1 + 1.0 / n
    if value < a:
        break
    print(f"1 + 1/{n} = {value:.3f}")
