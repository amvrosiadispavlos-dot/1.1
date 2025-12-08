n = int(input("Введите количество чисел n: "))
numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()[:n]))
count_equal = 0
count_zero_pairs = 0
count_even_pairs = 0
count_ends5_pairs = 0
for i in range(n - 1):
    a, b = numbers[i], numbers[i+1]
    if a == b:
        count_equal += 1
    if a == 0 and b == 0:
        count_zero_pairs += 1
    if a % 2 == 0 and b % 2 == 0:
        count_even_pairs += 1
    if a % 10 == 5 and b % 10 == 5:
        count_ends5_pairs += 1
print(f"а) Пар равных соседних чисел: {count_equal}")
print(f"б) Пар нулей: {count_zero_pairs}")
print(f"в) Пар чётных чисел: {count_even_pairs}")
print(f"г) Пар чисел, оканчивающихся на 5: {count_ends5_pairs}")
