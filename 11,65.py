arr = [15, 25, 30, 10, 40, 60, 5]
sum_gt_20 = sum(x for x in arr if x > 20)
sum_lt_50 = sum(x for x in arr if x < 50)
print(f"а) Сумма >20 = {sum_gt_20}, превышает 100: {sum_gt_20 > 100}")
print(f"б) Сумма <50 = {sum_lt_50}, четная: {sum_lt_50 % 2 == 0}")
