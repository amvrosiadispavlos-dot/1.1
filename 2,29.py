import math
x1, y1 = map(float, input("Введите координаты первой вершины (x1 y1): ").split())
x2, y2 = map(float, input("Введите координаты второй вершины (x2 y2): ").split())
x3, y3 = map(float, input("Введите координаты третьей вершины (x3 y3): ").split())
a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
perimeter = a + b + c
p = perimeter / 2
area = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Периметр треугольника: {perimeter:.4f}")
print(f"Площадь треугольника: {area:.4f}")
