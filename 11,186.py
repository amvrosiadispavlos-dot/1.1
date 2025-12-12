m = list(range(1, 13))
result = []
for i in range(6):
    result.append(m[i])
    result.append(m[11-i])
print(f"Результат: {result}")
