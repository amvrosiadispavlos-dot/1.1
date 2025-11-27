import math
R = 6350
print("Высота (км) | Расстояние до горизонта (км)")
print("-" * 45)
for h in range(1, 11):
    d = math.sqrt(2 * R * h + h**2)
    print(f"{h:2d}         | {d:8.2f}")
