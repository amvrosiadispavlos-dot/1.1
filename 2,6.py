import math
R = 6350
h = float(input("Введите высоту над Землей (в км): "))
distance = math.sqrt(h**2 + 2*R*h)
print(f"Расстояние до горизонта с высоты {h} км: {distance:.2f} км")
