import random
weights = [random.randint(40, 120) for _ in range(25)]
heavy = [w for w in weights if w > 100]
light = [w for w in weights if w <= 100]
avg_heavy = sum(heavy) / len(heavy) if heavy else 0
avg_light = sum(light) / len(light) if light else 0
print(f"Средняя масса полных (>100 кг): {avg_heavy:.1f}")
print(f"Средняя масса остальных: {avg_light:.1f}")
