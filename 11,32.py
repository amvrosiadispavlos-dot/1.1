import math
arr = [4, -9, 16, -25, 36, -49]
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
for i in range(len(arr_a)):
    if arr_a[i] < 0:
        arr_a[i] = abs(arr_a[i])
print("а) После замены отрицательных на модуль:", arr_a)

# б)
arr_b = arr.copy()
for i in range(len(arr_b)):
    if i % 2 != 0:  # нечетные индексы
        arr_b[i] = math.sqrt(abs(arr_b[i]))
print("б) После замены нечетных на корень:", arr_b)
