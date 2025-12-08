numbers = list(map(float, input("Введите 15 вещественных чисел через пробел: ").split()[:15]))
greater = [x for x in numbers if x > 10]
if greater:
    avg = sum(greater) / len(greater)
    print(f"Среднее чисел > 10: {avg}")
else:
    print("Нет чисел больше 10")
