arr = [10, 20, 30, 45, 50, 60, 70]
count = 0
for i in range(len(arr)-1):
    if arr[i] % 10 == 0 and arr[i+1] % 10 == 0:
        count += 1
print(f"Число пар соседей, оканчивающихся нулем: {count}")
