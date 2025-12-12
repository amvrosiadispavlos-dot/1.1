arr = [10, 20, 30, 40, 50]
index = int(input("Введите индекс: "))
if 0 <= index < len(arr):
    print(f"Элемент с индексом {index}: {arr[index]}")
else:
    print("Неверный индекс")
