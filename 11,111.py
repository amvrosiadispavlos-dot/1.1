arr = [2, 3, 5, 7, 2, 4, 9, 11, 13, 6, 15, 17, 19, 8]
max_length = 0
current_length = 0
for num in arr:
    if num % 2 != 0:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0
print(f"Массив: {arr}")
print(f"Наибольшая длина отрезка нечетных чисел: {max_length}")
