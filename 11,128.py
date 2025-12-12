import random
july_temps = [random.randint(15, 35) for _ in range(31)]
min_temp = min(july_temps)
count = july_temps.count(min_temp)
print(f"Количество самых прохладных дней ({min_temp}°C): {count}")
