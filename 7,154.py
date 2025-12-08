seq = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
max_count = 0
current_count = 0
prev = None
for num in seq:
    if num == prev:
        current_count += 1
    else:
        current_count = 1
        prev = num
    if current_count > max_count:
        max_count = current_count
print(f"Наибольшее количество подряд идущих одинаковых элементов: {max_count}")
