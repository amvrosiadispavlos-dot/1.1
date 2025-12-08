n = int(input("Введите количество спортсменов n (≥4): "))
times = list(map(float, input(f"Введите результаты {n} спортсменов (в сотых секунды) через пробел: ").split()[:n]))
sorted_times = sorted(times)
best_four_times = sorted_times[:4]
indices = []
for t in best_four_times:
    idx = times.index(t) + 1  
    indices.append(idx)
    times[idx-1] = -1  
indices.sort()
print(f"Индексы четырёх лучших бегунов: {indices}")
print(f"Их суммарное время: {sum(best_four_times)}")
