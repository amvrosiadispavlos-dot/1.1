import random
import math

def monte_carlo_area(func, x_min, x_max, y_max, n=1000000):
    count_inside = 0
    for _ in range(n):
        x = random.uniform(x_min, x_max)
        y = random.uniform(0, y_max)
        if y <= func(x):
            count_inside += 1
    area_rect = (x_max - x_min) * y_max
    return count_inside / n * area_rect

# а) Половина синусоиды (0 ≤ x ≤ π, 0 ≤ y ≤ sin(x))
area_a = monte_carlo_area(math.sin, 0, math.pi, 1)
print(f"а) Площадь под половиной синусоиды: {area_a:.6f}")
print(f"   Точное значение: 2.000000")

# б) Квадратная парабола y = x^2 (0 ≤ x ≤ 3, 0 ≤ y ≤ 9)
area_b = monte_carlo_area(lambda x: x**2, 0, 3, 9)
print(f"\nб) Площадь под параболой y=x^2 от 0 до 3: {area_b:.6f}")
print(f"   Точное значение: 9.000000")
