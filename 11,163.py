arr = [3, -5, 7, -2, 8, -1, 4, 10, -3]
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
i = 0
while i < len(arr_a):
    if arr_a[i] < 0:
        for j in range(i, len(arr_a)-1):
            arr_a[j] = arr_a[j+1]
        arr_a[-1] = 0
        # Не увеличиваем i, так как элементы сместились
    else:
        i += 1
print("а) После удаления всех отрицательных:", arr_a)

# б)
n = 6
arr_b = arr.copy()
i = 0
while i < len(arr_b):
    if arr_b[i] > n:
        for j in range(i, len(arr_b)-1):
            arr_b[j] = arr_b[j+1]
        arr_b[-1] = 0
    else:
        i += 1
print(f"б) После удаления всех элементов >{n}:", arr_b)

# в)
n1, n2 = 2, 5  # удаляем с 3-го по 6-й (индексы 2-5)
arr_c = arr.copy()
count = n2 - n1 + 1
for i in range(n1, len(arr_c)-count):
    arr_c[i] = arr_c[i+count]
for i in range(len(arr_c)-count, len(arr_c)):
    arr_c[i] = 0
print(f"в) После удаления элементов с {n1+1}-го по {n2+1}-й:", arr_c)
