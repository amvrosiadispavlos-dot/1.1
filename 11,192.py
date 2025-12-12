arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a = 45
result = [x for x in arr if x < a]
print(f"Элементы, меньшие {a}: {result}")

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
n = 45
for i in range(len(arr)-1):
    if arr[i] < n < arr[i+1]:
        print(f"Между элементами: arr[{i}]={arr[i]} и arr[{i+1}]={arr[i+1]}")
        break

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a = 45
closest_index = min(range(len(arr)), key=lambda i: abs(arr[i] - a))
print(f"Ближайший к {a}: arr[{closest_index}]={arr[closest_index]}")
