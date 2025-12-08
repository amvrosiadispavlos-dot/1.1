a = list(map(float, input("Введите 15 вещественных чисел по возрастанию через пробел: ").split()[:15]))
n = float(input("Введите число n (a₁ < n < a₁₅): "))
closest_index = 0
min_diff = float('inf')
for i in range(len(a)):
    diff = abs(a[i] - n)
    if diff < min_diff:
        min_diff = diff
        closest_index = i
print(f"Ближайший элемент к {n}: индекс {closest_index + 1}, значение {a[closest_index]}")
