last_year = float(input("Введите количество осадков за прошлый февраль: "))
print("Введите количество осадков за каждый день февраля (28 чисел):")
days = 28
precipitations = list(map(float, input().split()[:days]))
total = sum(precipitations)
print(f"Сумма осадков = {total}, превысила прошлогодние {last_year}: {total > last_year}")
