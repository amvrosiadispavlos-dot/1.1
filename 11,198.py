arr = [2, 4, 6, 8, 10, 12, 3, 5]
for i, x in enumerate(arr):
    if x % 2 != 0:
        print(f"Первый нечетный элемент: arr[{i}] = {x}")
        break
else:
    print("Нечетных элементов нет")

arr = [13, 26, 39, 52, 65]
for i, x in enumerate(arr):
    if x % 13 == 0:
        print(f"Первый элемент, кратный 13: arr[{i}] = {x}")
        break
else:
    print("Элементов, кратных 13, нет")
