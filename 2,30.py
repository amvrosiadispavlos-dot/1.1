import math
def triangle_area(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
x1, y1 = map(float, input("Введите координаты первой вершины (x1 y1): ").split())
x2, y2 = map(float, input("Введите координаты второй вершины (x2 y2): ").split())
x3, y3 = map(float, input("Введите координаты третьей вершины (x3 y3): ").split())
x4, y4 = map(float, input("Введите координаты четвертой вершины (x4 y4): ").split())
area1 = triangle_area(x1, y1, x2, y2, x3, y3)
area2 = triangle_area(x1, y1, x3, y3, x4, y4)
total_area = area1 + area2
print(f"Площадь четырехугольника: {total_area:.4f}")
