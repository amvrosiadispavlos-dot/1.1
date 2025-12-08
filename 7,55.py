n = int(input("Введите количество чисел n: "))
m = int(input("Введите число m: "))
q = int(input("Введите число q: "))
numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()[:n]))
sum_le_m = sum(x for x in numbers if x <= m)
cond = sum_le_m > q
print(f"Сумма чисел ≤ {m} = {sum_le_m}, превышает {q}: {cond}")
