print("Введите число детей в 1-м, 2-м, ..., 11-м классах (11 чисел через пробел):")
children = list(map(int, input().split()[:11]))
total_odd_classes = sum(children[i] for i in range(0, 11, 2))
print(f"Общее число детей в нечётных классах (1, 3, 5, ...): {total_odd_classes}")
