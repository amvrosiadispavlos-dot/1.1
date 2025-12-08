n = int(input("Введите количество чисел n: "))
p = float(input("Введите число p: "))
numbers = list(map(float, input(f"Введите {n} вещественных чисел через пробел: ").split()[:n]))
sum_gt_20_5 = sum(x for x in numbers if x > 20.5)
cond = sum_gt_20_5 < p
print(f"Сумма чисел > 20.5 = {sum_gt_20_5}, меньше {p}: {cond}")
