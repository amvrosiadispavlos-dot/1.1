import random
march_precip = [random.randint(0, 10) for _ in range(31)]
no_precip_days = sum(1 for x in march_precip if x == 0)
print(f"Дней без осадков: {no_precip_days}")
print(f"Верно, что не было 10 дней: {no_precip_days == 10}")
