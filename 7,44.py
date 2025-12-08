n = int(input("Введите количество чисел n: "))
numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()[:n]))
sum_even_pos = sum(numbers[i] for i in range(1, n, 2)) 
print(f"Сумма a₂ + a₄ + a₆ + ... : {sum_even_pos}")
