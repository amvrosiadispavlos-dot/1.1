print("Введите площади (га) 10 районов через пробел:")
areas = list(map(float, input().split()[:10]))
print("Введите урожайности (ц/га) 10 районов через пробел:")
yields = list(map(float, input().split()[:10]))
total_wheat = sum(areas[i] * yields[i] for i in range(10))
total_area = sum(areas)
avg_yield = total_wheat / total_area if total_area > 0 else 0
print(f"Общее количество пшеницы: {total_wheat:.2f} ц")
print(f"Средняя урожайность по области: {avg_yield:.2f} ц/га")
