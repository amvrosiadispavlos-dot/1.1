arr = [5, 25, 3, 40, 15, 60, 10]
print(f"Массив: {arr}")

# а)
sum_le_20 = sum(x for x in arr if x <= 20)
print(f"а) Сумма элементов ≤ 20: {sum_le_20}")

# б)
a = 30
sum_gt_a = sum(x for x in arr if x > a)
print(f"б) Сумма элементов > {a}: {sum_gt_a}")
