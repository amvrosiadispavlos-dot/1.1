m = int(input("Введите количество чисел m: "))
numbers = list(map(int, input(f"Введите {m} целых чисел через пробел: ").split()[:m]))
count_pos = sum(1 for x in numbers if x > 0)
print(f"Количество положительных чисел = {count_pos}, кратно 3: {count_pos % 3 == 0}")
