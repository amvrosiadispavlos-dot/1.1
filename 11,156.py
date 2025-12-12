arr = [10, 20, 30, 40, 50, 60]
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
if len(arr_a) >= 3:
    for i in range(2, len(arr_a)-1):
        arr_a[i] = arr_a[i+1]
    arr_a[-1] = 0
print("а) После удаления третьего элемента:", arr_a)

# б)
k = int(input("Введите номер элемента k для удаления (1-based): "))
arr_b = arr.copy()
if 1 <= k <= len(arr_b):
    for i in range(k-1, len(arr_b)-1):
        arr_b[i] = arr_b[i+1]
    arr_b[-1] = 0
print(f"б) После удаления {k}-го элемента:", arr_b)
