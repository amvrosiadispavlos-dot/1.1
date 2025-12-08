n = int(input("Введите количество чисел n (>3): "))
numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()[:n]))
max_sum = float('-inf')
min_sum = float('inf')
max_pair_indices = (0, 0)
min_pair_indices = (0, 0)
for i in range(n - 1):
    s = numbers[i] + numbers[i+1]
    if s > max_sum:
        max_sum = s
        max_pair_indices = (i+1, i+2)
    if s < min_sum:
        min_sum = s
        min_pair_indices = (i+1, i+2)
print(f"а) Максимальная сумма двух соседних чисел: {max_sum}")
print(f"б) Минимальная сумма двух соседних чисел: {min_sum}")
print(f"в) Номера первой пары с максимальной суммой: {max_pair_indices}")
print(f"г) Номера последней пары с минимальной суммой: {min_pair_indices}")
