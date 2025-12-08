distance = 10
day = 1
while distance <= 20:
    day += 1
    distance *= 1.1
print(f"Пробежит >20 км в {day} день")
daily_distance = 10
total = 10
day = 1
while total <= 100:
    day += 1
    daily_distance *= 1.1
    total += daily_distance
print(f"Суммарный пробег >100 км в {day} день")
