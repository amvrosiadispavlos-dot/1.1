days = int(input("Введите количество дней в месяце: "))
precip = list(map(float, input("Введите количество осадков за каждый день через пробел: ").split()[:days]))
max_precip = max(precip)
last_max_day = -1
for i in range(days):
    if precip[i] == max_precip:
        last_max_day = i + 1
print(f"Последний день с максимальным количеством осадков: {last_max_day}-е число")
