import math
arr = [4, 121, 9, 144, 16, 169, 25]
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
for i in range(len(arr_a)):
    if arr_a[i] > 10:
        arr_a[i] = math.sqrt(arr_a[i])
print("а) После замены >10 на корень:", arr_a)

# б)
arr_b = arr.copy()
for i in range(len(arr_b)):
    if i % 2 == 0: 
        arr_b[i] = abs(arr_b[i])
print("б) После замены четных на модуль:", arr_b)
