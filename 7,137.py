n = int(input("Введите количество городов: "))
max_dist = 0
for i in range(n):
    dist = float(input(f"Расстояние до города {i+1} (км): "))
    if dist > max_dist:
        max_dist = dist
print(f"Расстояние до самого удалённого города: {max_dist} км")
