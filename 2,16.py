import math
a = float(input("Введите первый катет a: "))
b = float(input("Введите второй катет b: "))
c = math.sqrt(a**2 + b**2)
P = a + b + c
print(f"Периметр треугольника: {P:.2f}")
