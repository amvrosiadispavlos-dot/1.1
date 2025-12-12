arr = [2, 5, 8, 3, 10, 7, 12, 15, 4, 9]
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
i = 0
while i < len(arr_a):
    if arr_a[i] % 2 == 0 and i % 2 == 0:  # четный элемент на четном месте (индекс четный)
        for j in range(i, len(arr_a)-1):
            arr_a[j] = arr_a[j+1]
        arr_a[-1] = 0
    else:
        i += 1
print("а) После удаления четных на нечетных местах:", arr_a)

# б)
arr_b = arr.copy()
i = 0
while i < len(arr_b):
    if arr_b[i] % 3 == 0 or arr_b[i] % 5 == 0:
        for j in range(i, len(arr_b)-1):
            arr_b[j] = arr_b[j+1]
        arr_b[-1] = 0
    else:
        i += 1
print("б) После удаления кратных 3 или 5:", arr_b)
