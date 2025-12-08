n = int(input("Введите количество чисел n: "))
numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()[:n]))
max_len = 0
current_len = 0
for num in numbers:
    if num % 2 == 0:
        current_len += 1
        max_len = max(max_len, current_len)
    else:
        current_len = 0
print(f"Наибольшая длина отрезка из чётных чисел: {max_len}")
