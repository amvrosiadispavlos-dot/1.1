import random
speeds = [random.randint(150, 300) for _ in range(40)]
sorted_speeds = sorted(speeds, reverse=True)
fastest_two = sorted_speeds[:2]
print(f"Скорости двух самых быстрых автомобилей: {fastest_two}")
