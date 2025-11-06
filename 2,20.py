import math
e = float(input("Введите e: "))
f = float(input("Введите f: "))
g = float(input("Введите g: "))
h = float(input("Введите h: "))
if f == 0:
    print("Ошибка: деление на ноль в a (f = 0).")
elif e - 3/f < 0:
    print("Ошибка: подкоренное выражение в a отрицательное.")
else:
    a_val = (math.sqrt(e - 3/f))**3 + g
    b_val = math.sin(e) + math.cos(h)**2
    if e*f - 3 == 0:
        print("Ошибка: деление на ноль в c.")
    else:
        c_val = (35 * g) / (e*f - 3)
        print(f"a = {a_val:.4f}")
        print(f"b = {b_val:.4f}")
        print(f"c = {c_val:.4f}")
