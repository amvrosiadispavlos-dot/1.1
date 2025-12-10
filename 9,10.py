n = 12 
m = 3  
salary = [[0] * m for _ in range(n)]
print("Введите зарплату каждого работника за 3 месяца (через пробел):")
for i in range(n):
    row = list(map(int, input(f"Работник {i+1}: ").split()))
    if len(row) != m:
        print(f"Нужно {m} чисел. Повторите.")
        row = list(map(int, input(f"Работник {i+1}: ").split()))
    salary[i] = row
max_salary = max(max(row) for row in salary)
total_per_worker = [sum(row) for row in salary]
max_total = max(total_per_worker)
worker_index = total_per_worker.index(max_total) + 1
monthly_totals = [sum(salary[i][j] for i in range(n)) for j in range(m)]
max_month_total = max(monthly_totals)
month_index = monthly_totals.index(max_month_total) + 1
print(f"\nа) Максимальная зарплата: {max_salary}")
print(f"б) Работник с наибольшей суммой: {worker_index}")
print(f"в) Месяц с максимальной общей зарплатой: {month_index}")
