arr = [1, 2, 3, 4, 5, 6]
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
half = len(arr_a) // 2
arr_a = arr_a[half:] + arr_a[:half]
print("а) Поменяны половины:", arr_a)

# б)
arr_b = arr.copy()
for i in range(0, len(arr_b), 2):
    if i+1 < len(arr_b):
        arr_b[i], arr_b[i+1] = arr_b[i+1], arr_b[i]
print("б) Поменяны пары:", arr_b)

# в)
arr_c = arr.copy()
for i in range(len(arr_c) // 2):
    arr_c[i], arr_c[-i-1] = arr_c[-i-1], arr_c[i]
print("в) Отражение относительно центра:", arr_c)
