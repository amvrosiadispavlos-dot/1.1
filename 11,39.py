arr = [10, 23, 30, 47, 50, 61, 70]
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
for i in range(len(arr_a)):
    if arr_a[i] % 10 == 0:
        arr_a[i] = 0
print("а) Элементы, кратные 10, заменены нулями:", arr_a)

# б)
arr_b = arr.copy()
for i in range(len(arr_b)):
    if arr_b[i] % 2 != 0:
        arr_b[i] *= 2
    else:
        arr_b[i] //= 2
print("б) Нечетные удвоены, четные уменьшены вдвое:", arr_b)

# в)
m = 2
n = 3
arr_c = arr.copy()
for i in range(len(arr_c)):
    if arr_c[i] % 2 != 0:
        arr_c[i] -= m
    if i % 2 != 0: 
        arr_c[i] += n
print("в) После преобразований с m и n:", arr_c)
