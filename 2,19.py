import math
a = float(input("Введите a: "))
b = float(input("Введите b: "))
denom1 = b + (a + b) / 2
if denom1 <= 0:
    print("Ошибка: подкоренное выражение должно быть > 0.")
elif a == 0:
    print("Ошибка: a не может быть 0 (деление на ноль в y).")
else:
    x = (a**2 + 25) / math.sqrt(denom1)
    y = (abs(a) + 2 * math.sin(b)) / (5.5 * a)
    print(f"x = {x:.4f}")
    print(f"y = {y:.4f}")
