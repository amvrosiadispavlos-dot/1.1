n = int(input("Введите количество команд: "))
points = list(map(int, input("Введите очки команд через пробел: ").split()[:n]))
min_points = min(points)
first_min_index = -1
for i in range(n):
    if points[i] == min_points:
        first_min_index = i + 1
        break
print(f"Первая команда с наименьшим количеством очков: №{first_min_index}")
