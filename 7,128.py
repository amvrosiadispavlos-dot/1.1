numbers = list(map(int, input("Введите 12 натуральных чисел через пробел: ").split()[:12]))
index_ends7 = -1
for i in range(len(numbers)):
    if numbers[i] % 10 == 7:
        index_ends7 = i + 1
        break
if index_ends7 != -1:
    print(f"Первое число, оканчивающееся на 7, на позиции {index_ends7}")
else:
    print("Нет чисел, оканчивающихся на 7")
