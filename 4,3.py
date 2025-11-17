import math
x = float(input("Введите x: "))
if x > 0:
    y = math.sin(x ** 2)
else:
    y = 1 + 2 * (math.sin(x) ** 2)
print(f"y = {y:.4f}")
