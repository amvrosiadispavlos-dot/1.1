precip = list(map(float, input("Введите осадки за 31 день марта через пробел: ").split()[:31]))
count_no_precip = sum(1 for p in precip if p == 0)
print(f"Дней без осадков = {count_no_precip}, равно 10: {count_no_precip == 10}")
