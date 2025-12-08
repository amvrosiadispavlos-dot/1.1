numbers = list(map(int, input("Введите 10 целых чисел через пробел: ").split()[:10]))
sum_ends_zero = sum(x for x in numbers if x % 10 == 0)
print(f"Сумма чисел, оканчивающихся нулём: {sum_ends_zero}")
