numbers = list(map(int, input("Введите 14 целых чисел через пробел: ").split()[:14]))
sum_gt_20 = sum(x for x in numbers if x > 20)
cond_a = sum_gt_20 > 100
print(f"а) Сумма чисел >20 = {sum_gt_20}, превышает 100: {cond_a}")
sum_lt_50 = sum(x for x in numbers if x < 50)
cond_b = sum_lt_50 % 2 == 0
print(f"б) Сумма чисел <50 = {sum_lt_50}, чётна: {cond_b}")
