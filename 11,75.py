arr = [10, 25, 35, 40, 55, 60, 75]
a = int(input("Введите a: "))
b = int(input("Введите b (b > a): "))
count = sum(1 for x in arr if a <= x <= b)
print(f"Элементов в интервале [{a}, {b}]: {count}")
