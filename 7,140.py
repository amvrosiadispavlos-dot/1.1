import math
n = int(input("Введите количество кругов: "))
min_radius = float('inf')
for i in range(n):
    area = float(input(f"Площадь круга {i+1}: "))
    radius = math.sqrt(area / math.pi)
    if radius < min_radius:
        min_radius = radius
print(f"Радиус самого маленького круга: {min_radius:.2f}")
