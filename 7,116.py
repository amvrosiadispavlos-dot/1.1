print("Введите стоимости автомобилей через пробел ($ > 5000):")
cars = list(map(float, input().split()))
print("Введите стоимости мотоциклов через пробел ($ < 5000):")
bikes = list(map(float, input().split()))
avg_cars = sum(cars) / len(cars) if cars else 0
avg_bikes = sum(bikes) / len(bikes) if bikes else 0
cond = avg_cars > 3 * avg_bikes
print(f"Средняя стоимость автомобилей: ${avg_cars:.2f}")
print(f"Средняя стоимость мотоциклов: ${avg_bikes:.2f}")
print(f"Автомобили дороже мотоциклов более чем в 3 раза: {cond}")
