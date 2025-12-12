arr = [5, 8, 3, 9, 2, 7, 9, 1]
max_val = max(arr)
min_val = min(arr)
max_index = arr.index(max_val)
min_index = arr.index(min_val)
if max_index < min_index:
    print("Максимальное число встретилось раньше")
elif min_index < max_index:
    print("Минимальное число встретилось раньше")
else:
    print("Максимальное и минимальное — одно и то же число")
