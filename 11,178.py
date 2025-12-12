arr = [1, 2, 3, 4, 5, 6, 7, 8]
s, k = 2, 6
element = arr[s-1]
for i in range(s, k):
    arr[i-1] = arr[i]
arr[k-1] = element
print(f"Результат: {arr}")
