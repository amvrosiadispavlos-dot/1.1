numbers = list(map(int, input("Введите ненулевые целые числа через пробел: ").split()))
if not numbers:
    print("Последовательность пуста")
else:
    sign_changes = 0
    for i in range(1, len(numbers)):
        if numbers[i-1] * numbers[i] < 0: 
            sign_changes += 1
    print(f"Количество смен знака: {sign_changes}")
