numbers = list(map(float, input("Введите 15 вещественных чисел через пробел: ").split()[:15]))
max_num = max(numbers)
print(f"а) Максимальное число: {max_num}")
min_num = min(numbers)
print(f"б) Минимальное число: {min_num}")
max_val = numbers[0]
min_val = numbers[0]
for num in numbers[1:]:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
print(f"в) Максимальное: {max_val}, Минимальное: {min_val}")
