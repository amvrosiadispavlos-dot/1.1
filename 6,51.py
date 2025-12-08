n = int(input("Введите натуральное число: "))
k = int(input("Введите k: "))
b = int(input("Введите b: "))
x = int(input("Введите x: "))
y = int(input("Введите y: "))
a = int(input("Введите a: "))
m = int(input("Введите m: "))
n_div_b = int(input("Введите n (для проверки делимости на n): "))
n_str = str(n)
digit_sum = 0
digit_product = 1
first_digit = int(n_str[0])
last_digit = int(n_str[-1])
for digit in n_str:
    digit_int = int(digit)
    digit_sum += digit_int
    digit_product *= digit_int
digit_count = len(n_str)
print("а) Сумма цифр > k и число четное:", digit_sum > k and n % 2 == 0)
print("б) Кол-во цифр четное и число ≤ b:", digit_count % 2 == 0 and n <= b)
print("г) Начинается на x и заканчивается на y:", first_digit == x and last_digit == y)
print("д) Произведение цифр < a и число делится на b:", digit_product < a and n % b == 0)
print("е) Сумма цифр > m и число делится на n:", digit_sum > m and n % n_div_b == 0)
