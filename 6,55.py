n = input("Введите натуральное число: ")
a = input("Введите цифру a: ")
b = input("Введите цифру b: ")
count_a = 0
count_b = 0
for digit in n:
    if digit == a:
        count_a += 1
    if digit == b:
        count_b += 1
print(f"Цифра {a} встречается реже, чем {b}:", count_a < count_b)
