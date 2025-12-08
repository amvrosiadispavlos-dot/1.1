numbers = list(map(int, input("Введите 9 целых чисел через пробел: ").split()[:9]))
sum_numbers = sum(numbers)
print(f"Сумма = {sum_numbers}, чётна: {sum_numbers % 2 == 0}")
