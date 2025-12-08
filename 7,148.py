n = int(input("Введите количество чисел n: "))
numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()[:n]))
max_num = max(numbers)
min_num = min(numbers)
cond = (max_num - min_num) <= 25
print(f"Максимальное: {max_num}, Минимальное: {min_num}")
print(f"Максимальное превышает минимальное не более чем на 25: {cond}")
