import random
july_precip = [random.randint(0, 20) for _ in range(31)]
max_precip = max(july_precip)
# a)
first_day = july_precip.index(max_precip) + 1
# б)
last_day = len(july_precip) - july_precip[::-1].index(max_precip)
print(f"Максимальное количество осадков: {max_precip} мм")
print(f"a) Первый самый дождливый день: {first_day} июля")
print(f"б) Последний самый дождливый день: {last_day} июля")
