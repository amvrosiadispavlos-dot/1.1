k = int(input("Введите количество чисел k: "))
numbers = list(map(int, input(f"Введите {k} целых чисел через пробел: ").split()[:k]))
last_index = -1
for i in range(k):
    if numbers[i] < 0:
        last_index = i + 1
print(f"Номер последнего отрицательного числа: {last_index}")
