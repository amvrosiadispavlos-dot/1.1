numbers = list(map(float, input("Введите 15 вещественных чисел через пробел: ").split()[:15]))
sum_neg_odd = -sum(numbers[i] for i in range(0, 15, 2))
print(f"-c₁ - c₃ - c₅ - ... = {sum_neg_odd}")
