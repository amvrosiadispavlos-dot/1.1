arr = list(range(1, 16))
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
arr_a[2:10] = arr_a[2:10][::-1]
print("а) Элементы с 3-го по 9-й в обратном порядке:", arr_a)

# б)
k = int(input("Введите k: "))
s = int(input("Введите s (s > k): "))
arr_b = arr.copy()
arr_b[k+1:s] = arr_b[k+1:s][::-1]
print(f"б) Элементы с {k+2}-го по {s-1}-й в обратном порядке:", arr_b)

# в)
arr_c = arr.copy()
min_index = arr_c.index(min(arr_c))
max_index = arr_c.index(max(arr_c))
start = min(min_index, max_index)
end = max(min_index, max_index)
arr_c[start:end+1] = arr_c[start:end+1][::-1]
print("в) Между мин и макс (включая) в обратном порядке:", arr_c)
