arr = [3, -5, 8, -2, 0, 7, -1]
positive = sum(1 for x in arr if x > 0)
negative = sum(1 for x in arr if x < 0)
print(f"Положительных: {positive}")
print(f"Отрицательных: {negative}")
