print("Введите последовательность целых чисел через пробел:")
numbers = list(map(int, input().split()))
if not numbers:
    print("Последовательность пуста")
else:
    first = numbers[0]
    count = 0
    for num in numbers:
        if num == first:
            count += 1
        else:
            break
    print(f"Количество одинаковых элементов в начале: {count}")
