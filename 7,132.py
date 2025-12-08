numbers = list(map(int, input("Введите 30 чисел (неубывающая последовательность) через пробел: ").split()[:30]))
unique_count = 1  
for i in range(1, len(numbers)):
    if numbers[i] != numbers[i-1]:
        unique_count += 1
print(f"Количество различных чисел: {unique_count}")
