numbers = list(map(int, input("Введите 12 целых чисел через пробел: ").split()[:12]))
all_equal = all(x == numbers[0] for x in numbers)
print(f"Все элементы последовательности равны: {all_equal}")
