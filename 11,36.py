arr = [5.0, -3.0, 0.0, 7.0, -4.0, 0.0, 9.0]
print("Исходный массив:", arr)

# а)
k1 = 0 
n = 2.5 
arr_a = arr.copy()
for i in range(len(arr_a)):
    if arr_a[i] > 0:
        arr_a[i] -= arr[k1]
    elif arr_a[i] < 0:
        arr_a[i] -= n
print("а) После преобразований:", arr_a)

# б)
n = 1.0 
a = 2.0 
b = 3.0
arr_b = arr.copy()
for i in range(len(arr_b)):
    if arr_b[i] == 0:
        arr_b[i] += n
    elif arr_b[i] > 0:
        arr_b[i] -= a
    else:
        arr_b[i] += b
print("б) После преобразований:", arr_b)
