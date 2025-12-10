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
print("\nа) День с максимальным доходом для каждого магазина:")
for i in range(n):
    max_day = income[i].index(max(income[i])) + 1
    print(f"   Магазин {i+1}: день {max_day}")
print("\nб) Магазин с максимальным доходом для каждого дня:")
for j in range(m):
    max_income = max(income[i][j] for i in range(n))
    shop_index = next(i + 1 for i in range(n) if income[i][j] == max_income)
    print(f"   День {j+1}: магазин {shop_index}")
