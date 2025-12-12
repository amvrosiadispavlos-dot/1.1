arr = [15, 25, 35, 45, 50, 65, 75]
a = 100
result = []
for x in arr:
    result.append(x)
    if '5' in str(x):
        result.append(a)
print(f"Исходный: {arr}")
print(f"Результат: {result}")
print(f"Макс. размер: {len(result)}")
