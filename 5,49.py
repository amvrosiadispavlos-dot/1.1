deposit = 1000
rate = 0.02
print("Месяц | Прирост | Сумма")
print("-" * 25)
for month in range(1, 11):
    increase = deposit * rate
    deposit += increase
    print(f"{month:2d}    | {increase:6.2f}  | {deposit:7.2f}")
deposit = 1000
rate = 0.02
print("Месяц | Сумма")
print("-" * 15)
for month in range(1, 13):
    deposit *= (1 + rate)
    if month >= 3:
        print(f"{month:2d}    | {deposit:7.2f}")
