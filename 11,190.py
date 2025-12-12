arr = [1000, 20000, 70000, 30000, 80000, 40000]
for i, val in enumerate(arr):
    if val > 65530:
        print(f"Номер первого > 65530: {i + 1}")
        break

arr = [1000, 20000, 70000, 30000, 80000, 40000]
for i in range(len(arr)-1, -1, -1):
    if arr[i] > 65530:
        print(f"Номер последнего > 65530: {i + 1}")
        break
