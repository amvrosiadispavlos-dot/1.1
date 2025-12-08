n = input("Введите натуральное число с разными цифрами: ")
max1 = max2 = -1
min1 = min2 = 10
for char in n:
    d = int(char)
    if d > max1:
        max2 = max1
        max1 = d
    elif d > max2:
        max2 = d
    if d < min1:
        min2 = min1
        min1 = d
    elif d < min2:
        min2 = d
print(f"а) Две максимальные цифры: {max1} и {max2}")
print(f"б) Две минимальные цифры: {min1} и {min2}")
