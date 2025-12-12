arr = [50, 45, 40, 35, 30, 25, 20]
first = arr.pop(0)
for i in range(len(arr)):
    if first >= arr[i]:
        arr.insert(i, first)
        break
else:
    arr.append(first)
print(f"Результат: {arr}")
