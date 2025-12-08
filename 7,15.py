numbers = list(map(float, input("Введите 10 вещественных чисел через пробел: ").split()[:10]))
sum_numbers = sum(numbers)
print(f"Сумма = {sum_numbers}, превышает 100.78: {sum_numbers > 100.78}")
