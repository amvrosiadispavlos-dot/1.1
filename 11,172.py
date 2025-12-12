arr = [3, 8, 1, 10, 4, 2, 9]
n = 5
m = 3
result = []
for x in arr:
    if x > n:
        result.append(n)
    result.append(x)
    if x < m:
        result.append(m)
print(f"Исходный: {arr}")
print(f"Результат: {result}")
print(f"Макс. размер: {len(result)}")
