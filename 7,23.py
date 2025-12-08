numbers = list(map(float, input("Введите 8 чисел через пробел: ").split()[:8]))
product = 1
for num in numbers:
    product *= num
print(f"Произведение = {product}, меньше 10000: {product < 10000}")
