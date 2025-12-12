arr = [3, -5, 7, -2, 8, -1, 4]
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
first_neg = next((i for i, x in enumerate(arr_a) if x < 0), None)
if first_neg is not None:
    for i in range(first_neg, len(arr_a)-1):
        arr_a[i] = arr_a[i+1]
    arr_a[-1] = 0
    print("а) После удаления первого отрицательного:", arr_a)
else:
    print("а) Отрицательных элементов нет")

# б)
arr_b = arr.copy()
last_even = next((i for i in range(len(arr_b)-1, -1, -1) if arr_b[i] % 2 == 0), None)
if last_even is not None:
    for i in range(last_even, len(arr_b)-1):
        arr_b[i] = arr_b[i+1]
    arr_b[-1] = 0
    print("б) После удаления последнего четного:", arr_b)
else:
    print("б) Четных элементов нет")
