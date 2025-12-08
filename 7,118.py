n = int(input("Введите количество чисел n: "))
numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()[:n]))
last_index = -1
for i in range(n):
    if numbers[i] == 10:
        last_index = i + 1  
first_index = -1
for i in range(n):
    if numbers[i] == 10:
        first_index = i + 1
        break
    print(f"а) Номер последнего числа 10: {last_index if last_index != -1 else 'нет'}")
print(f"б) Номер первого числа 10: {first_index if first_index != -1 else 'нет'}")
