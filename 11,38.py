arr = [14, 23, 34, 47, 54, 62, 74]
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
for i in range(len(arr_a)):
    if arr_a[i] % 10 == 4:
        arr_a[i] //= 2
print("а) Элементы, оканчивающиеся на 4, уменьшены вдвое:", arr_a)

# б)
arr_b = arr.copy()
for i in range(len(arr_b)):
    if arr_b[i] % 2 == 0:
        arr_b[i] **= 2
    else:
        arr_b[i] *= 2
print("б) Четные возведены в квадрат, нечетные удвоены:", arr_b)

# в)
a = 5
b = 3
arr_c = arr.copy()
for i in range(len(arr_c)):
    if arr_c[i] % 2 == 0:
        arr_c[i] += a
    if i % 2 == 0: 
        arr_c[i] -= b
print("в) После преобразований с a и b:", arr_c)
