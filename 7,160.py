n = int(input("Введите количество участников: "))
times = list(map(float, input("Введите результаты каждого участника через пробел: ").split()[:n]))
best_time = min(times)
first_best_index = -1
for i in range(n):
    if times[i] == best_time:
        first_best_index = i + 1
        break
print(f"Лучший результат показал спортсмен, стартовавший {first_best_index}-м")
