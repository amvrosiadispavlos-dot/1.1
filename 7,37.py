print("Введите количество жителей (тыс. чел.) 12 районов через пробел:")
population = list(map(float, input().split()[:12]))
print("Введите площади (км²) 12 районов через пробел:")
areas = list(map(float, input().split()[:12]))
total_population = sum(population)
total_area = sum(areas)
avg_density = total_population / total_area if total_area > 0 else 0
print(f"Средняя плотность населения по области: {avg_density:.2f} тыс. чел./км²")
