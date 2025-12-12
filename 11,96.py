arr = [4, 9, 2, 7, 5, 12, 8]
min_val = min(arr)
max_val = max(arr)
threshold = (min_val + max_val) / 2
indices = [i for i, x in enumerate(arr) if x > threshold]
print(f"Порог (среднее мин и макс): {threshold}")
print(f"Количество элементов > порога: {len(indices)}")
print(f"Их индексы: {indices}")
