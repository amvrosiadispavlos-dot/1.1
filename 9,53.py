from collections import defaultdict
cubes = [i**3 for i in range(1, 50)] 
sums = defaultdict(list)
for i in range(len(cubes)):
    for j in range(i+1, len(cubes)):
        s = cubes[i] + cubes[j]
        sums[s].append((i+1, j+1))
found = False
for num in sorted(sums.keys()):
    if len(sums[num]) >= 2:
        print(f"Наименьшее число: {num}")
        print(f"Способы:")
        for a, b in sums[num]:
            print(f"  {a}^3 + {b}^3 = {a**3} + {b**3}")
        found = True
        break
if not found:
    print("Такое число не найдено в заданном диапазоне.")
