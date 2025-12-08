n = int(input("Введите натуральное число: "))
a = int(input("Введите a: "))
b = int(input("Введите b: "))
k = int(input("Введите k: "))
m = int(input("Введите m: "))
n_str = str(n)
digit_sum = 0
digit_product = 1
first_digit = int(n_str[0])
for digit in n_str:
    digit_int = int(digit)
    digit_sum += digit_int
    digit_product *= digit_int
digit_count = len(n_str)
print("а) Сумма цифр < a:", digit_sum < a)
print("б) Произведение цифр > b:", digit_product > b)
print("в) Число k-значное:", digit_count == k)
print("г) Первая цифра превышает m:", first_digit > m)
