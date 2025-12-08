speeds = list(map(int, input("Введите максимальные скорости 12 марок автомобилей (км/ч) через пробел: ").split()[:12]))
max1 = max(speeds)
max2 = float('-inf')
for s in speeds:
    if s > max2 and s != max1:
        max2 = s
print(f"Скорость автомобиля, больше которой только максимальная: {max2} км/ч")
