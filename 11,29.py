import random
precipitation = [random.randint(0, 10) for _ in range(31)]
no_precip_days = [day+1 for day, precip in enumerate(precipitation) if precip == 0]
print("Дни без осадков:", no_precip_days)
