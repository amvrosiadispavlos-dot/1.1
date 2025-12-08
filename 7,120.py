n = int(input("Введите количество чисел n: "))
numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()[:n]))
last_index = -1
for i in range(n):
    if numbers[i] == 25:
        last_index = i + 1
if last_index != -1:
    print(f"Номер последнего числа 25: {last_index}")
else:
    print("Чисел, равных 25, нет.")
