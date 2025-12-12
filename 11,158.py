arr = [15, 7, 23, 9, 42, 18]
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
max_val = max(arr_a)
max_index = arr_a.index(max_val)
for i in range(max_index, len(arr_a)-1):
    arr_a[i] = arr_a[i+1]
arr_a[-1] = 0
print("а) После удаления максимального:", arr_a)

# б)
arr_b = arr.copy()
min_val = min(arr_b)
min_index = arr_b.index(min_val)
for i in range(min_index, len(arr_b)-1):
    arr_b[i] = arr_b[i+1]
arr_b[-1] = 0
print("б) После удаления минимального:", arr_b)
