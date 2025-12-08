numbers = list(map(int, input("Введите 20 чисел (неубывающая последовательность) через пробел: ").split()[:20]))
repeats = 0
for i in range(1, len(numbers)):
    if numbers[i] == numbers[i-1]:
        repeats += 1
print(f"Количество повторений чисел: {repeats}")
