a = float(input("Введите a (1 < a <= 1.5): "))
n = 2
print(f"n, при которых 1 + 1/n ≥ {a}:")
while True:
    value = 1 + 1.0 / n
    if value >= a:
        print(n, end=' ')
    else:
        break
    n += 1
print()
