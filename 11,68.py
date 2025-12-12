arr = [3, -1, 0, -5, 7, -2, 4]
non_negative_count = sum(1 for x in arr if x >= 0)
print(f"Количество неотрицательных элементов: {non_negative_count}")
