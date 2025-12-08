n = int(input("Введите количество чисел n: "))
numbers = list(map(float, input(f"Введите {n} чисел через пробел: ").split()[:n]))
sum_lt_25_5 = sum(x for x in numbers if x < 25.5)
cond_a = sum_lt_25_5 <= 50
print(f"а) Сумма чисел < 25.5 = {sum_lt_25_5}, не превышает 50: {cond_a}")
sum_le_20 = sum(x for x in numbers if x <= 20)
cond_b = sum_le_20 % 3 == 0
print(f"б) Сумма чисел ≤ 20 = {sum_le_20}, кратна 3: {cond_b}")
