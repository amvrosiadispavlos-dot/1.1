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
print("\nа) Месяц с наибольшей зарплатой для каждого работника:")
for i in range(n):
    max_sal = max(salary[i])
    month_index = salary[i].index(max_sal) + 1
    print(f"   Работник {i+1}: месяц {month_index}")
print("\nб) Работник с наибольшей зарплатой для каждого месяца:")
for j in range(m):
    max_sal = max(salary[i][j] for i in range(n))
    worker_index = next(i + 1 for i in range(n) if salary[i][j] == max_sal)
    print(f"   Месяц {j+1}: работник {worker_index}")
