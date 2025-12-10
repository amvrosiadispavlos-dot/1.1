n = 5  
m = 6   
sales = [[0] * m for _ in range(n)]
print("Введите доход от продажи каждого вида товара за 6 дней (через пробел):")
for i in range(n):
    row = list(map(int, input(f"Товар {i+1}: ").split()))
    if len(row) != m:
        print(f"Нужно {m} чисел. Повторите.")
        row = list(map(int, input(f"Товар {i+1}: ").split()))
    sales[i] = row
print("\nа) Общий доход по каждому виду товара:")
for i in range(n):
    total = sum(sales[i])
    print(f"   Товар {i+1}: {total}")
print("\nб) Общий доход за каждый день:")
for j in range(m):
    total = sum(sales[i][j] for i in range(n))
    print(f"   День {j+1}: {total}")
total_all = sum(sum(row) for row in sales)
print(f"\nв) Общий доход магазина за 6 дней: {total_all}")
total_per_good = [sum(row) for row in sales]
max_good_total = max(total_per_good)
max_good_index = total_per_good.index(max_good_total) + 1
print(f"г) Товар с максимальным общим доходом: {max_good_index}")
day_totals = [sum(sales[i][j] for i in range(n)) for j in range(m)]
max_day_total = max(day_totals)
max_day_index = day_totals.index(max_day_total) + 1
print(f"д) День с максимальным общим доходом: {max_day_index}")
a = int(input("\nВведите значение a для пункта 'е': "))
days_above_a = sum(1 for total in day_totals if total > a)
print(f"е) Количество дней с доходом выше {a}: {days_above_a}")
