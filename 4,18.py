import math
circle_area = float(input("Площадь круга: "))
square_area = float(input("Площадь квадрата: "))
circle_radius = math.sqrt(circle_area / math.pi)
circle_diameter = 2 * circle_radius
square_side = math.sqrt(square_area)
square_diagonal = square_side * math.sqrt(2)
if circle_diameter <= square_side:
    print("а) Круг поместится в квадрате")
else:
    print("а) Круг не поместится в квадрате")
if square_diagonal <= circle_diameter:
    print("б) Квадрат поместится в круге")
else:
    print("б) Квадрат не поместится в круге")
