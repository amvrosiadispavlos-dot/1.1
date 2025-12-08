numbers = list(map(float, input("Введите 10 чисел через пробел: ").split()[:10]))
average = sum(numbers) / len(numbers)
print("Среднее арифметическое:", average)
