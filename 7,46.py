n = int(input("Введите количество чисел n: "))
numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()[:n]))
a1_plus_an = numbers[0] + numbers[-1]
print(f"а) a₁ + aₙ = {a1_plus_an}")
if n >= 2:
    a2_minus_anm1 = numbers[1] - numbers[-2]
    print(f"б) a₂ - aₙ₋₁ = {a2_minus_anm1}")
else:
    print("б) Недостаточно элементов для вычисления a₂ - aₙ₋₁")
