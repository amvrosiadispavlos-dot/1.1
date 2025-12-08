n = 22  
results = list(map(float, input(f"Введите результаты {n} спортсменов (в секундах) через пробел: ").split()[:n]))
sorted_results = sorted(results)
first = sorted_results[0]
second = sorted_results[1]
print(f"Первое место: {first} с")
print(f"Второе место: {second} с")
