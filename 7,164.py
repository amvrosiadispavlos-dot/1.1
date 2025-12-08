import math
n = int(input("Введите количество пар n: "))
max_avg = -1
last_max_index = -1
min_geom = float('inf')
first_min_index = -1
for i in range(n):
    a, b = map(float, input(f"Пара {i+1} (a b): ").split())
    avg = (a + b) / 2
    if avg >= max_avg:
        max_avg = avg
        last_max_index = i + 1
    geom = math.sqrt(a * b)
    if geom < min_geom:
        min_geom = geom
        first_min_index = i + 1
print(f"а) Последняя пара с максимальным средним арифметическим: №{last_max_index}")
print(f"б) Первая пара с минимальным средним геометрическим: №{first_min_index}")
