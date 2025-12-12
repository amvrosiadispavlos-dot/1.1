import random
feb_temps = [random.randint(-10, 5) for _ in range(28)]
sorted_temps = sorted(feb_temps)
coldest_two = sorted_temps[:2]
dates = []
for temp in coldest_two:
    dates.append(feb_temps.index(temp) + 1)
print(f"Даты двух самых холодных дней: {dates}")
