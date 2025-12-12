arr = [3, -5, 7, -2, 8, -1, 4]
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
first_neg = next((i for i, x in enumerate(arr_a) if x < 0), None)
if first_neg is not None:
    arr_a.append(0)
    for i in range(len(arr_a)-1, first_neg+1, -1):
        arr_a[i] = arr_a[i-1]
    arr_a[first_neg+1] = 99 
    print("а) После вставки после первого отрицательного:", arr_a)
else:
    print("а) Отрицательных элементов нет")

# б)
arr_b = arr.copy()
last_even = next((i for i in range(len(arr_b)-1, -1, -1) if arr_b[i] % 2 == 0), None)
if last_even is not None:
    arr_b.append(0)
    for i in range(len(arr_b)-1, last_even, -1):
        arr_b[i] = arr_b[i-1]
    arr_b[last_even] = 77 
    print("б) После вставки перед последним четным:", arr_b)
else:
    print("б) Четных элементов нет")
