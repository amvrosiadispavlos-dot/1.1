import math
radius = float(input("Введите радиус круга: "))
side = float(input("Введите сторону квадрата: "))
circle_area = math.pi * radius ** 2
square_area = side ** 2
if circle_area > square_area:
    print("Площадь круга больше")
else:
    print("Площадь квадрата больше")
