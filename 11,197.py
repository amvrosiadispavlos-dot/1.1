arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = 5
if n in arr:
    index = arr.index(n)
    print(f"Элементы перед первым {n}: {arr[:index]}")
else:
    print(f"Элемент {n} не найден, все элементы: {arr}")

arr = [17, 23, 27, 34, 47, 52, 67]
last_index = -1
for i in range(len(arr)-1, -1, -1):
    if str(arr[i])[-1] == '7':
        last_index = i
        break
if last_index != -1 and last_index < len(arr)-1:
    print(f"Элементы после последнего, оканчивающегося на 7: {arr[last_index+1:]}")
else:
    print("Нет элементов для вывода")
