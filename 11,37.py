arr = [4.0, -2.0, 0.0, -5.0, 0.0, 8.0, -1.0]
print("Исходный массив:", arr)

# а)
a1 = 0 
b = 3.0 
arr_a = arr.copy()
for i in range(len(arr_a)):
    if arr_a[i] < 0:
        arr_a[i] += arr[a1]
    elif arr_a[i] == 0:
        arr_a[i] -= b
print("а) После преобразований:", arr_a)

# б)
a = 2.0 
b = 1.5 
c = 0.5 
arr_b = arr.copy()
for i in range(len(arr_b)):
    if arr_b[i] > 0:
        arr_b[i] -= a
    elif arr_b[i] < 0:
        arr_b[i] -= b
    else:
        arr_b[i] += c
print("б) После преобразований:", arr_b)
