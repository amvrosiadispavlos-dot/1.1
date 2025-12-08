n = int(input("Введите количество чисел n: "))
numbers = list(map(float, input(f"Введите {n} чисел через пробел: ").split()[:n]))
sum_squares = sum(x**2 for x in numbers)
print("Сумма квадратов:", sum_squares)
