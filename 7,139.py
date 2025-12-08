speeds = list(map(int, input("Введите максимальные скорости 20 марок автомобилей через пробел: ").split()[:20]))
max_speed = max(speeds)
print(f"Самый быстрый автомобиль имеет скорость: {max_speed} км/ч")
