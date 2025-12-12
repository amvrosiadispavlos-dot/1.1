import random
feb_precip = [random.randint(0, 5) for _ in range(28)]
no_precip_days = sum(1 for x in feb_precip if x == 0)
print(f"Количество дней без осадков: {no_precip_days}")
