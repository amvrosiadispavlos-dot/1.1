a = float(input("Введите a (1 < a <= 1.5): "))
n = 2
while True:
    value = 1 + 1.0 / n
    if value < a:
        break
    print(f"1 + 1/{n} = {value:.3f}")
    n += 1
