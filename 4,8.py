import math
x = float(input("Введите x: "))
if math.sin(x) >= 0:
    k = x ** 2
else:
    k = abs(x)
if x < k:
    f = abs(x)
else:
    f = k * x
print(f"k = {k:.4f}")
print(f"f(x) = {f:.4f}")
