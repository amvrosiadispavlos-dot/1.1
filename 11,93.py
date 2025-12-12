import random
cars = [random.randint(5001, 30000) for _ in range(10)]
motorcycles = [random.randint(1000, 5000) for _ in range(15)]
avg_car = sum(cars) / len(cars)
avg_moto = sum(motorcycles) / len(motorcycles)
print(f"Средняя стоимость авто: {avg_car:.0f}")
print(f"Средняя стоимость мотоциклов: {avg_moto:.0f}")
print(f"Превышает более чем в 3 раза: {avg_car > 3 * avg_moto}")
