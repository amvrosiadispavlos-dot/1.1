arr = [4, -2, 7, 5, -8, 0, 3]
print("Массив:", arr)

# а)
s = 2
if 0 <= s < len(arr):
    print(f"а) Элемент с индексом {s} ({arr[s]}) положительный: {arr[s] > 0}")

# б)
k = 3
if 0 <= k < len(arr):
    print(f"б) Элемент с индексом {k} ({arr[k]}) четный: {arr[k] % 2 == 0}")

# в)
k = 1
s = 4
if 0 <= k < len(arr) and 0 <= s < len(arr):
    if arr[k] > arr[s]:
        print(f"в) Элемент {k} ({arr[k]}) больше элемента {s} ({arr[s]})")
    elif arr[s] > arr[k]:
        print(f"в) Элемент {s} ({arr[s]}) больше элемента {k} ({arr[k]})")
    else:
        print(f"в) Элементы {k} и {s} равны")
