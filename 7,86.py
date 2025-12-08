n = int(input("Введите количество чисел n: "))
numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()[:n]))
count_lt20 = sum(1 for x in numbers if x < 20)
print(f"Количество чисел < 20 = {count_lt20}, равно 5: {count_lt20 == 5}")
