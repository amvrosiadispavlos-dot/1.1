n = int(input("Введите количество чисел n (>3): "))
numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()[:n]))
max1 = max2 = float('-inf')
for x in numbers:
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2:
        max2 = x
min1 = min2 = float('inf')
for x in numbers:
    if x < min1:
        min2 = min1
        min1 = x
    elif x < min2:
        min2 = x
print(f"а) Два максимальных элемента: {max1}, {max2}")
print(f"б) Два минимальных элемента: {min1}, {min2}")
