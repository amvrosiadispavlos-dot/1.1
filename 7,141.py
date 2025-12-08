import math
n = int(input("Введите количество квадратов: "))
max_diagonal = 0
for i in range(n):
    area = float(input(f"Площадь квадрата {i+1}: "))
    side = math.sqrt(area)
    diagonal = side * math.sqrt(2)
    if diagonal > max_diagonal:
        max_diagonal = diagonal
print(f"Длина диагонали самого большого квадрата: {max_diagonal:.2f}")
