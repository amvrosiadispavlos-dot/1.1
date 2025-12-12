arr = [1, 2, 3, 4, 5, 6, 7, 8]
s, k = 6, 2
element = arr[s-1]
for i in range(s-1, k-1, -1):
    arr[i] = arr[i-1]
arr[k-1] = element
print(f"Результат: {arr}")
