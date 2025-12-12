import random
july_temps = [random.randint(15, 35) for _ in range(31)]
sorted_temps = sorted(july_temps, reverse=True)
top_two_temps = sorted_temps[:2]
dates = []
for temp in top_two_temps:
    dates.append(july_temps.index(temp) + 1)
print(f"Даты двух самых теплых дней: {dates}")
