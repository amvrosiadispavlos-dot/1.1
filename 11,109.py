arr = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6]
print("Массив:", arr)
count_equal_neighbors = 0
i = 0
while i < len(arr):
    j = i
    while j < len(arr) and arr[j] == arr[i]:
        j += 1
    if j - i > 1:
        count_equal_neighbors += (j - i)
    i = j
unique_count = len(set(arr))
print(f"Количество элементов с равными соседями: {count_equal_neighbors}")
print(f"Количество различных чисел: {unique_count}")
