arr = [12, 45, 3, 78, 23, 56]
print("Исходный массив:", arr)
arr_copy = arr.copy()

max_val = max(arr_copy)
max_index = arr_copy.index(max_val)
for i in range(max_index, len(arr_copy)-1):
    arr_copy[i] = arr_copy[i+1]
arr_copy[-1] = 0


min_val = min(arr_copy[:-1]) 
min_index = arr_copy.index(min_val)
for i in range(min_index, len(arr_copy)-1):
    arr_copy[i] = arr_copy[i+1]
arr_copy[-1] = 0

print("После удаления макс и мин:", arr_copy[:-1])  
