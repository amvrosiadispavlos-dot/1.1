arr = [5, 3, 8, 6, 2]
for i in range(len(arr)-1):
    if arr[i+1] < arr[i]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
print(f"Массив после прохода: {arr}")
print(f"Последний элемент: {arr[-1]}")
