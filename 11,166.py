arr = [1, 2, 3, 4, 5]
print("Исходный массив:", arr)

# а)
arr_a = arr.copy()
k = 1  
arr_a.append(0)  # увеличиваем размер
for i in range(len(arr_a)-1, k+1, -1):
    arr_a[i] = arr_a[i-1]
arr_a[k+1] = 10
print("а) После вставки 10 после второго элемента:", arr_a)

# б)
m = 3 
arr_b = arr.copy()
arr_b.append(0)
for i in range(len(arr_b)-1, m+1, -1):
    arr_b[i] = arr_b[i-1]
arr_b[m+1] = 100
print(f"б) После вставки 100 после {m+1}-го элемента:", arr_b)
