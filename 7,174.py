points = list(map(int, input("Введите очки 12 команд через пробел: ").split()[:12]))
sorted_points = sorted(points, reverse=True)
first, second, third = sorted_points[0], sorted_points[1], sorted_points[2]
print(f"Первое место: {first} очков")
print(f"Второе место: {second} очков")
print(f"Третье место: {third} очков")
