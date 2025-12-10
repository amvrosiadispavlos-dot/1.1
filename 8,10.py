a = float(input("Введите a: "))
n = 1
print(f"Числа 1 + 1/n < {a}:")
while True:
    if n == 1:
        value = 1.0
    else:
        value = 1 + 1.0 / n
    if value < a:
        print(f"1 + 1/{n} = {value:.3f}")
    else:
        if n == 1:
            n += 1
            continue
        else:
            break
    n += 1
