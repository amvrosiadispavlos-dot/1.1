n = input("Введите натуральное число: ")
a = input("Введите цифру a: ")
b = input("Введите цифру b: ")
k = int(input("Введите k: "))
count_a = 0
count_b = 0
has_a = False
has_b = False
for digit in n:
    if digit == a:
        count_a += 1
        has_a = True
    if digit == b:
        count_b += 1
        has_b = True
print("а) Есть ли цифра a:", has_a)
print("б) Верно ли, что нет цифры b:", not has_b)
print("в) Цифра a встречается более k раз:", count_a > k)
print("г) Есть ли цифры a и b:", has_a and has_b)
