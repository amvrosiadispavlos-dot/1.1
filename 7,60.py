n = int(input("Введите количество дней в месяце: "))
temps = list(map(float, input("Введите температуры через пробел: ").split()[:n]))
count_below_zero = sum(1 for t in temps if t < 0)
print(f"Температура опускалась ниже 0°C {count_below_zero} раз(а)")
