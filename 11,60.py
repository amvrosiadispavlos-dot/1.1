arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Массив: {arr}")

# а)
sum_odd = sum(x for x in arr if x % 2 != 0)
print(f"а) Сумма нечетных: {sum_odd}")

# б)
k = 3
sum_multiple_k = sum(x for x in arr if x % k == 0)
print(f"б) Сумма кратных {k}: {sum_multiple_k}")

# в)
a = 2
b = 5
sum_multiple_a_or_b = sum(x for x in arr if x % a == 0 or x % b == 0)
print(f"в) Сумма кратных {a} или {b}: {sum_multiple_a_or_b}")
