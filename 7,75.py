import math
g = 9.8
R = float(input("Расстояние до цели R (м): "))
H = float(input("Высота цели H (м): "))
P = float(input("Высота цели P (м): "))
n = int(input("Количество пар (α, v₀): "))
hits = 0
for i in range(n):
    alpha = float(input(f"  Угол α (град) для выстрела {i+1}: "))
    v0 = float(input(f"  Начальная скорость v₀ (м/с) для выстрела {i+1}: "))
    alpha_rad = math.radians(alpha)
    t = R / (v0 * math.cos(alpha_rad))
    y = v0 * t * math.sin(alpha_rad) - g * t**2 / 2
    if H <= y <= H + P:
        hits += 1
percentage = (hits / n) * 100 if n > 0 else 0
print(f"Процент попаданий: {percentage:.2f}%")
