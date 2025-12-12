import random
car_capacity = 5000 
item_masses = [random.randint(50, 300) for _ in range(30)]
total_mass = sum(item_masses)
print(f"Грузоподъемность авто: {car_capacity} кг")
print(f"Общая масса груза: {total_mass} кг")
print(f"Не превышает: {total_mass <= car_capacity}")
