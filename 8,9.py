a = float(input("Введите a (1 < a <= 1.5): "))
n = 2
while True:
    value = 1 + 1.0 / n
    if value < a:
        print(f"Наименьшее n, при котором 1 + 1/n < {a}: {n}")
        break
    n += 1
