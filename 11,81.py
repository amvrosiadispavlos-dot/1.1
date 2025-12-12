arr = [2, 4, 3, 6, 8, 10, 5]
count = 0
for i in range(len(arr)-1):
    if arr[i] % 2 == 0 and arr[i+1] % 2 == 0:
        count += 1
print(f"Число пар четных соседей: {count}")
