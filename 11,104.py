import random
july_temps = [random.randint(15, 35) for _ in range(31)]
print("Температуры июля:", july_temps)
max_sum = 0
start_day = 0
for i in range(len(july_temps)-6):
    current_sum = sum(july_temps[i:i+7])
    if current_sum > max_sum:
        max_sum = current_sum
        start_day = i
print(f"Самые теплые 7 дней с {start_day+1} по {start_day+7} июля")
print(f"Температуры: {july_temps[start_day:start_day+7]}")
