arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 45]
last = arr.pop()
for i in range(len(arr)-1, -1, -1):
    if last >= arr[i]:
        arr.insert(i+1, last)
        break
else:
    arr.insert(0, last)
print(f"Результат: {arr}")
