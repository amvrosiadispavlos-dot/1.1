arr = [5, 8, -3, -7, 10, 12, -4, 6]
n = 0
result = [arr[0]]
for i in range(1, len(arr)):
    if (arr[i-1] > 0 and arr[i] > 0) or (arr[i-1] < 0 and arr[i] < 0):
        result.append(n)
    result.append(arr[i])
print(f"Исходный: {arr}")
print(f"Результат: {result}")
print(f"Макс. размер: {len(result)}")
