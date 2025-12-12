arr = [3, -5, 8, -2, 7, -4, 9]
positive = [x for x in arr if x > 0]
negative = [x for x in arr if x < 0]
avg_pos = sum(positive) / len(positive) if positive else 0
avg_neg = sum(negative) / len(negative) if negative else 0
print(f"Среднее положительных: {avg_pos:.2f}")
print(f"Среднее отрицательных: {avg_neg:.2f}")
