n = int(input("Введите натуральное число: "))
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
print("а) Сумма цифр > 10:", digit_sum > 10)
print("б) Произведение цифр < 50:", digit_product < 50)
print("в) Количество цифр четное:", digit_count % 2 == 0)
print("г) Число четырехзначное:", digit_count == 4)
print("д) Первая цифра не превышает 6:", first_digit <= 6)
print("е) Начинается и заканчивается одной цифрой:", first_digit == last_digit)
print("ж) Первая цифра больше последней:", first_digit > last_digit)
