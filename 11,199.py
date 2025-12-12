arr = [1.5, 2.3, -3.7, 4.2, 5.1, -6.8]
for i, x in enumerate(arr):
    if x < 0:
        print(f"Первый отрицательный: arr[{i}] = {x}")
        print(f"Элементы после него: {arr[i+1:]}")
        break
else:
    print("Отрицательных чисел нет")

arr = [1.5, -2.3, 3.7, 4.2, -5.1, 6.8]
for i in range(len(arr)-1, -1, -1):
    if arr[i] < 0:
        print(f"Последний отрицательный: arr[{i}] = {arr[i]}")
        print(f"Элементы слева от него: {arr[:i]}")
        break
else:
    print("Отрицательных чисел нет")
