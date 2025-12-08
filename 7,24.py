n = int(input("Введите количество чисел n: "))
s = float(input("Введите число s: "))
numbers = list(map(float, input(f"Введите {n} вещественных чисел через пробел: ").split()[:n]))
product = 1
for num in numbers:
    product *= num
print(f"Произведение = {product}, больше {s}: {product > s}")
