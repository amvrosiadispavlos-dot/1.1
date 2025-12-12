arr = [3, -5, 7, -2, 8, -1, 4]
print("Исходный массив:", arr)

first_negative = next((i for i, x in enumerate(arr) if x < 0), None)
last_positive = next((i for i in range(len(arr)-1, -1, -1) if arr[i] > 0), None)

if first_negative is not None and last_positive is not None:
    arr[first_negative], arr[last_positive] = arr[last_positive], arr[first_negative]
    print("После обмена:", arr)
else:
    print("Не хватает отрицательных или положительных элементов")
