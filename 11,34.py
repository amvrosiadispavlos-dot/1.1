arr = [3.5, -2.1, 7.8, -4.3, 9.1, 6.2]
print("Исходный массив:", arr)

# а)
k1 = 1 
k2 = 2 
arr_a = arr.copy()
for i in range(len(arr_a)):
    if arr_a[i] > 0:
        arr_a[i] -= arr[k1]
    else:
        arr_a[i] -= arr[k2]
print("а) После вычитания:", arr_a)

# б)
arr_b = arr.copy()
for i in range(len(arr_b)):
    if i % 2 != 0:  
        arr_b[i] += 1
    else:
        arr_b[i] -= 1
print("б) После изменения на ±1:", arr_b)
