numbers = list(map(float, input("Введите 16 вещественных чисел через пробел: ").split()[:16]))
greater_than_20 = [x for x in numbers if x > 20]
average = sum(greater_than_20) / len(greater_than_20)
print(f"Среднее арифметическое чисел > 20: {average}")
