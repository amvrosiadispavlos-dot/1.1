arr = [3, -7, 5, 9, -12, 8]
max_abs_index = max(range(len(arr)), key=lambda i: abs(arr[i]))
arr[max_abs_index] = -arr[max_abs_index]
print(f"Массив после изменения знака у максимального по модулю: {arr}")
