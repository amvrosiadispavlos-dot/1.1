n = 16 
min_density = float('inf')
for i in range(n):
    population = float(input(f"Численность населения государства {i+1} (млн чел): "))
    area = float(input(f"Площадь государства {i+1} (тыс. км²): "))
    density = population / area if area > 0 else float('inf')
    if density < min_density:
        min_density = density
print(f"Минимальная плотность населения: {min_density:.2f} млн чел. / тыс. км²")
