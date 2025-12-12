import random
monthly_precipitation = [random.randint(20, 150) for _ in range(12)]
months_indices = [2, 5, 8, 11]  
total_selected = sum(monthly_precipitation[i] for i in months_indices)
print(f"Осадки по месяцам: {monthly_precipitation}")
print(f"Сумма осадков в марте, июне, сентябре и декабре: {total_selected}")
