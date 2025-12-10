n = 3  
m = 10 
income = [[0] * m for _ in range(n)]
print("Введите доход каждого магазина за 10 дней (через пробел):")
for i in range(n):
    row = list(map(int, input(f"Магазин {i+1}: ").split()))
    if len(row) != m:
        print(f"Нужно {m} чисел. Повторите.")
        row = list(map(int, input(f"Магазин {i+1}: ").split()))
    income[i] = row
total_per_shop = [sum(row) for row in income]
max_total_shop = total_per_shop.index(max(total_per_shop)) + 1
day_totals = [sum(income[i][j] for i in range(n)) for j in range(m)]
max_day = day_totals.index(max(day_totals)) + 1
max_income_value = max(max(row) for row in income)
for i in range(n):
    if max_income_value in income[i]:
        max_shop = i + 1
        max_day_shop = income[i].index(max_income_value) + 1
        break
print(f"\nа) Магазин с максимальным общим доходом: {max_total_shop}")
print(f"б) День с максимальным общим доходом фирмы: {max_day}")
print(f"в) Максимальный доход за день: магазин {max_shop}, день {max_day_shop}")
