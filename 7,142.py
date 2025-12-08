n = 20
max_density = 0
for i in range(n):
    mass = float(input(f"Масса тела {i+1} (кг): "))
    volume = float(input(f"Объём тела {i+1} (см³): ")) / 1e6
    density = mass / volume if volume > 0 else 0
    if density > max_density:
        max_density = density
print(f"Максимальная плотность материала: {max_density:.2f} кг/м³")
