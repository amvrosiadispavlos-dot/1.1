a = float(input("Введите a: "))
s = 0.0
n = 1
while s <= a:
    s += 1.0 / n
    n += 1
print(f"Наименьшее n, при котором сумма > {a}: {n-1}")
print(f"Сумма = {s:.5f}")
