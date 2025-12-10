n = 12  
m = 3 
salary_table = [[0] * m for _ in range(n)]
print("Введите зарплату каждого работника за каждый месяц (через пробел для каждого месяца):")
for i in range(n):
    months_salary = list(map(int, input(f"Работник {i+1} (месяцы 1-{m}): ").split()))
    if len(months_salary) != m:
        print(f"Ошибка: нужно ввести ровно {m} значения. Повторите ввод.")
        months_salary = list(map(int, input(f"Работник {i+1} (месяцы 1-{m}): ").split()))
    salary_table[i] = months_salary
total_all = sum(sum(row) for row in salary_table)
quarter_salary_per_worker = [sum(row) for row in salary_table]
monthly_total = [sum(salary_table[i][j] for i in range(n)) for j in range(m)]
print("\nРезультаты:")
print(f"а) Общая сумма за квартал всем работникам: {total_all}")
print("б) Зарплата за квартал каждого работника:")
for i in range(n):
    print(f"   Работник {i+1}: {quarter_salary_per_worker[i]}")
print("в) Общая зарплата всех работников по месяцам:")
for j in range(m):
    print(f"   Месяц {j+1}: {monthly_total[j]}")
