import random
precip_per_year = [random.randint(500, 900) for _ in range(15)]
avg_precip = sum(precip_per_year) / 15
deviations = [(year+1, precip, precip - avg_precip) 
              for year, precip in enumerate(precip_per_year)]
print(f"Среднее количество осадков: {avg_precip:.1f}")
for year, precip, dev in deviations:
    print(f"Год {year}: {precip} мм, отклонение: {dev:+.1f}")
