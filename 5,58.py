import math
x_intersect = math.sqrt(2.5) - 2
n = 1000
width = x_intersect / n
area = 0
for i in range(n):
    x = i * width
    y = 0.4 * (x + 2)**2 + 1
    area += (y - 0) * width  
print(f"Площадь фигуры: {area:.4f}")
