m = int(input("Введите количество чисел m: "))
n = int(input("Введите число n: "))
numbers = list(map(int, input(f"Введите {m} целых чисел через пробел: ").split()[:m]))
multiples = [x for x in numbers if x % n == 0]
average = sum(multiples) / len(multiples)
print(f"Среднее арифметическое чисел, кратных {n}: {average}")
