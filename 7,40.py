numbers = list(map(float, input("Введите 12 вещественных чисел через пробел: ").split()[:12]))
sum_greater = sum(x for x in numbers if x > 10.75)
print(f"Сумма чисел > 10.75: {sum_greater}")
