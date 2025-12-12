arr = [1, 3, 2, 5, 4, 6, 3]
count = 0
for i in range(1, len(arr)-1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        count += 1
print(f"Элементов, больших соседей: {count}")
