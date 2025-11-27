cells = 1
print("Время (ч) | Количество клеток")
print("-" * 25)
for hours in range(3, 25, 3):
    cells *= 2
    print(f"{hours:2d}       | {cells:2d}")
