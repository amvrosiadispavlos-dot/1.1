n = int(input("Введите количество чисел n: "))
numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()[:n]))
max_val = max(numbers)
min_val = min(numbers)
max_first_index = -1
min_first_index = -1
for i in range(n):
    if numbers[i] == max_val and max_first_index == -1:
        max_first_index = i
    if numbers[i] == min_val and min_first_index == -1:
        min_first_index = i
if max_first_index < min_first_index:
    print("Максимальное число встретилось раньше минимального")
else:
    print("Минимальное число встретилось раньше максимального")
