days = 31
temperatures = list(map(float, input(f"Введите температуры за {days} дней июля через пробел: ").split()[:days]))
sorted_temps = sorted(temperatures)
coolest1, coolest2 = sorted_temps[0], sorted_temps[1]
date1 = temperatures.index(coolest1) + 1
temperatures[date1 - 1] = float('inf')
date2 = temperatures.index(coolest2) + 1
print(f"Два самых прохладных дня: {date1}-е и {date2}-е июля")
