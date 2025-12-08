numbers = list(map(int, input("Введите 20 чисел (неубывающая последовательность) через пробел: ").split()[:20]))
equal_count = 0
i = 0
while i < len(numbers):
    j = i + 1
    while j < len(numbers) and numbers[j] == numbers[i]:
        j += 1
    if j - i > 1:
        equal_count += (j - i)  # все числа в группе повторяются
    i = j
print(f"Количество чисел, идущих подряд и равных между собой: {equal_count}")
