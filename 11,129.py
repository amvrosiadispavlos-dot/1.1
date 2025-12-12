arr = [4, 7, 2, 7, 2, 9, 2, 9]
min_val = min(arr)
max_val = max(arr)
min_indices = [i for i, x in enumerate(arr) if x == min_val]
max_indices = [i for i, x in enumerate(arr) if x == max_val]
print(f"Массив: {arr}")
print(f"a) Номера минимальных элементов: {min_indices}")
print(f"б) Номера максимальных элементов: {max_indices}")
