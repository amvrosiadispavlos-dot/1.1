import random
points = [random.randint(0, 100) for _ in range(20)]
sorted_points = sorted(points, reverse=True)
first_second = sorted_points[:2]
first_index = points.index(first_second[0]) + 1
second_index = points.index(first_second[1]) + 1
print(f"Команда на первом месте (индекс {first_index}): {first_second[0]} очков")
print(f"Команда на втором месте (индекс {second_index}): {first_second[1]} очков")
