import math
circle_area = float(input("Площадь круга: "))
triangle_area = float(input("Площадь треугольника: "))
circle_radius = math.sqrt(circle_area / math.pi)
triangle_side = math.sqrt(4 * triangle_area / math.sqrt(3))
inscribed_radius = triangle_side * math.sqrt(3) / 6
if circle_radius <= inscribed_radius:
    print("а) Круг поместится в треугольнике")
else:
    print("а) Круг не поместится в треугольнике")
circumscribed_radius = triangle_side * math.sqrt(3) / 3
if circumscribed_radius <= circle_radius:
    print("б) Треугольник поместится в круге")
else:
    print("б) Треугольник не поместится в круге")
