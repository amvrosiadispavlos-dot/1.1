n = int(input("Введите количество чисел n: "))
m = int(input("Введите число m: "))
p = int(input("Введите число p: "))
numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()[:n]))
sum_le_m = sum(x for x in numbers if x <= m)
cond = sum_le_m % p == 0
print(f"Сумма чисел ≤ {m} = {sum_le_m}, кратна {p}: {cond}")
