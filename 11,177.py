arr = [1, 2, 3, 4, 5, 6]
k = 4
first = arr[0]
for i in range(1, k):
    arr[i-1] = arr[i]
arr[k-1] = first
print(f"Результат: {arr}")
