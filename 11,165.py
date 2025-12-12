arr = [2, 5, 2, 8, 5, 3, 8, 1]
print("Исходный массив:", arr)
seen = set()
i = 0
while i < len(arr):
    if arr[i] in seen:
        for j in range(i, len(arr)-1):
            arr[j] = arr[j+1]
        arr[-1] = 0
    else:
        seen.add(arr[i])
        i += 1
print("После удаления повторяющихся (оставлены первые вхождения):", arr[:len(seen)])
