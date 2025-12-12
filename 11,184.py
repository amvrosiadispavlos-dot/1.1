arr = [120, 130, 140, 150, 160, 170, 145, 190, 200, 210]
k = 7  
element = arr.pop(k-1)
for i in range(len(arr)):
    if element <= arr[i]:
        arr.insert(i, element)
        break
else:
    arr.append(element)
print(f"Результат: {arr}")
