m = int(input("Введите количество чисел m: "))
n = int(input("Введите число n: "))
numbers = list(map(int, input(f"Введите {m} целых чисел через пробел: ").split()[:m]))
multiples = [x for x in numbers if x % n == 0]
if multiples:
    avg = sum(multiples) / len(multiples)
    print(f"Среднее чисел, кратных {n}: {avg}")
else:
    print(f"Нет чисел, кратных {n}")
