numbers = list(map(int, input("Введите 14 целых чисел через пробел: ").split()[:14]))
max_even = float('-inf')
for num in numbers:
    if num % 2 == 0 and num > max_even:
        max_even = num
if max_even != float('-inf'):
    print(f"Максимальное чётное число: {max_even}")
else:
    print("Чётных чисел нет.")
