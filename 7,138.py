days = int(input("Введите количество дней в месяце: "))
temperatures = list(map(float, input(f"Введите температуру за каждый день через пробел: ").split()[:days]))
max_temp = max(temperatures)
print(f"Максимальная температура месяца: {max_temp}°C")
