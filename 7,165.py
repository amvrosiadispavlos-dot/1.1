n = 25 
max_speed = -1
best_car_index = -1
for i in range(n):
    distance = float(input(f"Расстояние для автомобиля {i+1} (км): "))
    time = float(input(f"Время для автомобиля {i+1} (ч): "))
    speed = distance / time if time > 0 else 0
    if speed > max_speed:
        max_speed = speed
        best_car_index = i + 1
print(f"Автомобиль с максимальной средней скоростью: №{best_car_index}")
