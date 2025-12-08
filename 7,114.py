numbers = list(map(int, input("Введите 14 целых чисел через пробел: ").split()[:14]))
even = [x for x in numbers if x % 2 == 0]
if even:
    avg = sum(even) / len(even)
    print(f"Среднее чётных чисел: {avg}")
else:
    print("Нет чётных чисел")
