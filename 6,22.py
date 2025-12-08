n = int(input("n (>99) = "))
while n >= 1000:
    n //= 10
third_digit = n % 10
print("Третья цифра:", third_digit)
