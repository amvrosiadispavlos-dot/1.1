import math
e = float(input("Введите e: "))
f = float(input("Введите f: "))
g = float(input("Введите g: "))
h = float(input("Введите h: "))
a_val = (e + f/2) / 3
b_val = abs(h**2 - g)
under_sqrt = (g - h)**2 - 3 * math.sin(e)
if under_sqrt < 0:
    print("Ошибка: подкоренное выражение в c отрицательное.")
else:
    c_val = math.sqrt(under_sqrt)
    print(f"a = {a_val:.4f}")
    print(f"b = {b_val:.4f}")
    print(f"c = {c_val:.4f}")
