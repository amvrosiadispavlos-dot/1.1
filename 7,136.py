n = int(input("Введите количество спортсменов: "))
best_time = float('inf')
for i in range(n):
    time = float(input(f"Результат спортсмена {i+1} (в минутах): "))
    if time < best_time:
        best_time = time
    print(f"Лучший результат после {i+1} спортсмена: {best_time} мин")
