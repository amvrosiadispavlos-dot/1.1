n = int(input("Введите количество чисел n: "))
numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()[:n]))
max_val = max(numbers)
last_max_index = -1
for i in range(n):
    if numbers[i] == max_val:
        last_max_index = i + 1
min_val = min(numbers)
first_min_index = -1
for i in range(n):
    if numbers[i] == min_val:
        first_min_index = i + 1
        break
print(f"а) Номер последнего максимального числа: {last_max_index}")
print(f"б) Номер первого минимального числа: {first_min_index}")
