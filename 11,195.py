arr = [5, 5, 5, 5, 3, 7, 2, 9, 1]
first_element = arr[0]
count = arr.count(first_element)
print(f"Количество одинаковых элементов в начале: {count}")
print(f"Элементы после них: {arr[count:]}")
