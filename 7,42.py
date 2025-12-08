numbers = list(map(int, input("Введите 10 целых чисел через пробел: ").split()[:10]))
sum_even = sum(x for x in numbers if x % 2 == 0)
print(f"Сумма чётных чисел: {sum_even}")
