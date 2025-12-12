arr = [3, 7, 2, 9, 5, 8]
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
arr_a[1], arr_a[4] = arr_a[4], arr_a[1]
print("а) Поменяны второй и пятый:", arr_a)

# б)
m = 0  # первый
n = 3  # четвертый
arr_b = arr.copy()
arr_b[m], arr_b[n] = arr_b[n], arr_b[m]
print(f"б) Поменяны {m+1}-й и {n+1}-й:", arr_b)

# в)
arr_c = arr.copy()
max_val = max(arr_c)
max_index = arr_c.index(max_val)
arr_c[2], arr_c[max_index] = arr_c[max_index], arr_c[2]
print("в) Поменяны третий и первый максимальный:", arr_c)

# г)
arr_d = arr.copy()
min_val = min(arr_d)
min_index = len(arr_d) - 1 - arr_d[::-1].index(min_val)
arr_d[0], arr_d[min_index] = arr_d[min_index], arr_d[0]
print("г) Поменяны первый и последний минимальный:", arr_d)
