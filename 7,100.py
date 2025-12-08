numbers = list(map(float, input("Введите 15 вещественных чисел через пробел: ").split()[:15]))
for i in range(len(numbers) - 1):
    if numbers[i] >= numbers[i+1]:
        print(f"Последовательность не упорядочена по возрастанию.")
        print(f"Первое число, нарушающее порядок: позиция {i+2} (число {numbers[i+1]})")
        break
else:
    print("Последовательность упорядочена по возрастанию.")
