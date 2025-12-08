deposit = 1000
rate = 0.02
month = 0
increase = 0
while increase <= 30:
    month += 1
    increase = deposit * rate
    deposit += increase
print(f"Увеличение превысит 30 руб. в {month} месяц")
deposit = 1000
rate = 0.02
month = 0
while deposit <= 1200:
    month += 1
    deposit *= (1 + rate)
print(f"Вклад превысит 1200 руб. через {month} месяцев")
