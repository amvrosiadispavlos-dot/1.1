import random
october_precip = [random.randint(0, 25) for _ in range(31)]
max_precip = max(october_precip)
count = october_precip.count(max_precip)
print(f"Количество дней с максимальными осадками ({max_precip} мм): {count}")
