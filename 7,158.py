m = int(input("Введите количество чисел m: "))
numbers = list(map(int, input(f"Введите {m} целых чисел через пробел: ").split()[:m]))
max_val = max(numbers)
min_val = min(numbers)
last_max_index = -1
last_min_index = -1
for i in range(m):
    if numbers[i] == max_val:
        last_max_index = i + 1
    if numbers[i] == min_val:
        last_min_index = i + 1
print(f"Номер последнего максимального числа: {last_max_index}")
print(f"Номер последнего минимального числа: {last_min_index}")
