a = list(map(float, input("Введите 15 вещественных чисел через пробел: ").split()[:15]))
first_neg_index = -1
for i in range(len(a)):
    if a[i] < 0:
        first_neg_index = i + 1
        break
if first_neg_index != -1:
    print(f"Первое отрицательное число на позиции {first_neg_index}")
else:
    print("Отрицательных чисел нет.")
