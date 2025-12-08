n = int(input("Введите количество покупателей: "))
t = list(map(float, input("Введите время обслуживания каждого покупателя через пробел: ").split()[:n]))
c = []
total_wait = 0
for i in range(n):
    c.append(total_wait)
    total_wait += t[i]
min_service_time = min(t)
last_min_index = -1
for i in range(n):
    if t[i] == min_service_time:
        last_min_index = i + 1
print("Время пребывания в очереди для каждого покупателя:")
for i in range(n):
    print(f"Покупатель {i+1}: {c[i]:.2f} мин")
print(f"Последний покупатель с минимальным временем обслуживания: №{last_min_index}")
