arr = [10, 20, 30, 40, 50]
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
arr_a = [x - 20 for x in arr_a]
print("а) Уменьшены на 20:", arr_a)

# б)
arr_b = arr.copy()
last = arr_b[-1]
arr_b = [x * last for x in arr_b]
print("б) Умножены на последний элемент:", arr_b)

# в)
B = 5
arr_c = arr.copy()
arr_c = [x + B for x in arr_c]
print("в) Увеличены на B:", arr_c)
