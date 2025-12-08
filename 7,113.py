n = int(input("Введите число n: "))
numbers = list(map(int, input("Введите 12 целых чисел через пробел: ").split()[:12]))
greater = [x for x in numbers if x > n]
if greater:
    avg = sum(greater) / len(greater)
    print(f"Среднее чисел > {n}: {avg}")
else:
    print(f"Нет чисел больше {n}")
