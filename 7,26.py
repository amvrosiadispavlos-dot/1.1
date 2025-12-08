n = int(input("Введите количество чисел n: "))
numbers = list(map(float, input(f"Введите {n} чисел через пробел: ").split()[:n]))
average = sum(numbers) / n
print("Среднее арифметическое:", average)
