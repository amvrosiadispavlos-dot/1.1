arr = [4, 8, 12, 6, 10]
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
arr_a = [x * 2 for x in arr_a]
print("а) Увеличены в 2 раза:", arr_a)

# б)
A = 3
arr_b = arr.copy()
arr_b = [x - A for x in arr_b]
print("б) Уменьшены на A:", arr_b)

# в)
arr_c = arr.copy()
if arr_c[0] != 0:
    arr_c = [x / arr_c[0] for x in arr_c]
    print("в) Разделены на первый элемент:", arr_c)
else:
    print("в) Первый элемент равен 0, деление невозможно")
