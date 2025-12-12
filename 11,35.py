arr = [1.5, -3.2, 4.7, -5.1, 6.3, -2.8]
print("Исходный массив:", arr)

# а)
m1 = 0  
m2 = 1
arr_a = arr.copy()
for i in range(len(arr_a)):
    if arr_a[i] < 0:
        arr_a[i] += arr[m1]
    else:
        arr_a[i] += arr[m2]
print("а) После прибавления:", arr_a)

# б)
arr_b = arr.copy()
for i in range(len(arr_b)):
    if i % 2 == 0:  
        arr_b[i] *= 2
    else:
        arr_b[i] -= 1
print("б) После удвоения/уменьшения:", arr_b)
