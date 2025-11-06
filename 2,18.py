import math
x = float(input("Введите x: "))
y = float(input("Введите y: "))
if x == 0:
    print("Ошибка: x не может быть 0 (деление на ноль в z).")
else:
    z = (x + (2 + y) / (x**2)) / (y + 1 / math.sqrt(x**2 + 10))
    q = 7.25 * math.sin(x) - abs(y)
    print(f"z = {z:.4f}")
    print(f"q = {q:.4f}")
