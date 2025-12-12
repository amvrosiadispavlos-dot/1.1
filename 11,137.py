arr = [5, 8, 3, 8, 9, 2, 9]

# a) 
max1 = max(arr)
arr_without_max = [x for x in arr if x != max1]
max2 = max(arr_without_max) if arr_without_max else max1
print(f"a) Максимальный: {max1}, второй максимальный: {max2}")

# б) 
min1 = min(arr)
arr_without_min = [x for x in arr if x != min1]
min2 = min(arr_without_min) if arr_without_min else min1
print(f"б) Минимальный: {min1}, второй минимальный: {min2}")

# в) 
max_val = max(arr)
max_indices = [i for i, x in enumerate(arr) if x == max_val]
first_max_index = max_indices[0]
if len(max_indices) > 1:
    second_max_index = max_indices[1]
else:
    second_max = max(x for x in arr if x < max_val)
    second_max_index = arr.index(second_max)
print(f"в) Индекс первого максимального: {first_max_index}, второго максимального: {second_max_index}")

# г) 
min_val = min(arr)
min_indices = [i for i, x in enumerate(arr) if x == min_val]
first_min_index = min_indices[0]
if len(min_indices) > 1:
    second_min_index = min_indices[1]
else:
    second_min = min(x for x in arr if x > min_val)
    second_min_index = arr.index(second_min)
print(f"г) Индекс первого минимального: {first_min_index}, второго минимального: {second_min_index}")
