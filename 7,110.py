masses = list(map(float, input("Введите массы людей через пробел: ").split()))
full = [m for m in masses if m > 100]
others = [m for m in masses if m <= 100]
avg_full = sum(full) / len(full) if full else 0
avg_others = sum(others) / len(others) if others else 0
print(f"Средняя масса полных (>100 кг): {avg_full:.2f} кг")
print(f"Средняя масса остальных: {avg_others:.2f} кг")
