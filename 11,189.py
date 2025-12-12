arr = [1, 3, 5, 7, 9, 5, 2, 4]
index = arr.index(5) if 5 in arr else -1
print(f"Номер первого элемента = 5: {index + 1}")

arr = [1, 3, 5, 7, 9, 5, 2, 4]
index = len(arr) - 1 - arr[::-1].index(5) if 5 in arr else -1
print(f"Номер последнего элемента = 5: {index + 1}")
