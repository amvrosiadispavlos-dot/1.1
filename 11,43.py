arr = [1, 2, 3, 4, 5, 6]
alternating_sum = 0
sign = 1
for x in arr:
    alternating_sum += sign * x
    sign *= -1
print(f"Массив: {arr}")
print(f"Знакопеременная сумма: {alternating_sum}")
