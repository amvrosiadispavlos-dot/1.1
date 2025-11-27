import math
x1 = 1 - math.sqrt(10/3)
x2 = 1 + math.sqrt(10/3)
n = 1000
width = (x2 - x1) / n
area = 0
for i in range(n):
    x = x1 + i * width
    y = 0.3 * (x - 1)**2 + 3
    area += (y - 2) * width
print(f"Площадь фигуры: {area:.4f}")
