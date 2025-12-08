n = int(input("Введите количество чисел n: "))
numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()[:n]))
last_index = -1
for i in range(n):
    if numbers[i] > 100:
        last_index = i + 1
print(f"Номер последнего числа > 100: {last_index}")
