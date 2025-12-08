n = int(input("Введите количество чисел n: "))
numbers = list(map(float, input(f"Введите {n} чисел через пробел: ").split()[:n]))
print("Сумма:", sum(numbers))
