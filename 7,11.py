numbers = list(map(float, input("Введите 8 чисел через пробел: ").split()[:8]))
product = 1
for num in numbers:
    product *= num
print("Произведение:", product)
