m = int(input("Введите количество чисел m: "))
numbers = list(map(int, input(f"Введите {m} целых чисел через пробел: ").split()[:m]))
last_index = -1
for i in range(m):
    if abs(numbers[i]) % 100 == 12:  
        last_index = i + 1
if last_index != -1:
    print(f"Номер последнего числа, оканчивающегося на 12: {last_index}")
else:
    print("Таких чисел нет.")
