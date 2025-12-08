numbers = list(map(int, input("Введите 10 целых чисел через пробел: ").split()[:10]))
count_pos = sum(1 for x in numbers if x > 0)
print(f"Количество положительных чисел = {count_pos}, не превышает 5: {count_pos <= 5}")
