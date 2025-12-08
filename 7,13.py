numbers = list(map(float, input("Введите 10 чисел через пробел: ").split()[:10]))
sum_squares = sum(x**2 for x in numbers)
print("Сумма квадратов:", sum_squares)
